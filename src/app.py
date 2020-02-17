from flask import Flask, url_for, redirect, request
from pm_core import PortManager, ProcessManager
from pm_log import LogUtil


app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect(url_for('static', filename='index.html'))

@app.route('/update', methods=['GET', 'POST'])
def update():
    form_info = request.form.to_dict()
    port_num = form_info.get('port_number')
    logger = LogUtil()
    logger.info("received new port number is :" + port_num)

    manager = PortManager('/etc/shadowsocks.json')
    manager.update_port_number(port_num)
    logger.info("update done")

    process_mgr = ProcessManager()
    pid = process_mgr.find_ssr_process_id()
    process_mgr.kill_and_restart_ssr(pid)
    return "Greeting, may the Force be with you!"

if __name__ == '__main__':
    app.run(debug="true", host="0.0.0.0", port="8000")