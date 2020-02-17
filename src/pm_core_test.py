import unittest
import json

from pm_core import PortManager
from pm_log import LogUtil

class PortManagerTest(unittest.TestCase):
    def test_update_port_number(self):
        manager = PortManager('/Users/kelvinmak/workspace/PortManager/src/cfg/shadowsocks.json')
        manager.update_port_number(6969)
        self.assertTrue(self.validate_port_num(6969))

    def validate_port_num(self, port_num):
        logger = LogUtil()

        with open('/Users/kelvinmak/workspace/PortManager/src/cfg/shadowsocks.json', 'r') as json_file:
            content = json.load(json_file)
            port_num_updated = content['server_port']
            logger.debug(port_num_updated)
        json_file.close
        
        if port_num_updated == port_num:
            return True
        else:
            return False    
        
        
if __name__ == '__main__':
    unittest.main()