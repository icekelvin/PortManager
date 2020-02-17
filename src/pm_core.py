import json
import os
import time
import logging
from pm_log import LogUtil

class PortManager:

    def __init__(self, json_cfg):
        self.json_cfg = json_cfg
    
    def get_json_content(self):
        with open(self.json_cfg, 'r') as json_file:
            content = json.load(json_file)
            
        json_file.close
        return content
    
    def rewrite_json_content(self, json_content, port_numb):
        with open(self.json_cfg, 'w') as json_file:
            json_content['server_port'] = port_numb
            json.dump(json_content, json_file)
        json_file.close


    def update_port_number(self, port_num):
        json_content = self.get_json_content()
        self.rewrite_json_content(json_content, port_num)

    def send_mail(self):
        pass


class ProcessManager:
    def find_ssr_process_id(self):
        pid = os.popen('ps -ef | grep server.py').readlines()[0].split()[1]
        logger = LogUtil()
        logger.info('SSR process id is :' + pid)
        return pid
    
    def kill_and_restart_ssr(self, pid):
        os.system('kill -9 ' + pid)
        time.sleep(5)
        os.system('python /usr/local/shadowsocks/server.py -c /etc/shadowsocks.json -d start')

