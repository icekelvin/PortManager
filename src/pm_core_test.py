import unittest
import json
import os

from pm_core import PortManager, Configuration
from pm_log import LogUtil

class PortManagerTest(unittest.TestCase):

    def test_update_port_number(self):
        self.json_file = os.path.dirname(os.path.abspath(__file__)) + os.sep + "cfg" + os.sep + "shadowsocks.json"
        logger = LogUtil()
        logger.debug(self.json_file)

        manager = PortManager(self.json_file)
        manager.update_port_number(6969)
        self.assertTrue(self.validate_port_num(6969))

    def validate_port_num(self, port_num):
        logger = LogUtil()

        with open(self.json_file, 'r') as json_file:
            content = json.load(json_file)
            port_num_updated = content['server_port']
            logger.debug(port_num_updated)
        json_file.close
        
        if port_num_updated == port_num:
            return True
        else:
            return False   

    def test_config_parse(self): 
        cfg = Configuration()
        ssr_config_loc = cfg.getConfig('SSR')
        self.assertEqual('/etc/shadowsocks.json', ssr_config_loc)

        ssr_test_config_loc = cfg.getConfig('SSR_Test')
        self.assertEqual('/Users/kelvinmak/workspace/PortManager/src/cfg/shadowsocks.json', ssr_test_config_loc)

if __name__ == '__main__':
    unittest.main()