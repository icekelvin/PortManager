import json
import os
import time
import logging
import ConfigParser

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
    def restart_ssr(self):
        os.system('python /usr/local/shadowsocks/server.py -c /etc/shadowsocks.json -d restart')

class Configuration: 
    def __init__(self):
        current_path = os.path.dirname(os.path.realpath(__file__)) + os.sep + 'cfg'
        print('current_path: {}'.format(current_path))
        cfg = os.path.join(current_path, 'setting.ini')
        self.conf = ConfigParser.ConfigParser()
        self.conf.read(cfg)
        
    def getConfig(self, selection):
        return self.conf.get(selection, 'config')
        



