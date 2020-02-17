import logging
import logging.handlers
import os
import time
 
class LogUtil:
    def __init__(self):
        self.logger = logging.getLogger("")

        logs_dir="log"
        if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
            pass
        else:
            os.mkdir(logs_dir)
        
        timestamp = time.strftime("%Y-%m-%d",time.localtime())
        logfilename = '%s.txt' % timestamp
        logfilepath = os.path.join(logs_dir,logfilename)
        rotatingFileHandler = logging.handlers.RotatingFileHandler(filename =logfilepath,
                                                                   maxBytes = 1024 * 1024 * 50,
                                                                   backupCount = 5)
        
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        rotatingFileHandler.setFormatter(formatter)

        console = logging.StreamHandler()
        console.setLevel(logging.NOTSET)
        console.setFormatter(formatter)

        self.logger.addHandler(rotatingFileHandler)
        self.logger.addHandler(console)
        self.logger.setLevel(logging.NOTSET)
 
    def info(self, message):
        self.logger.info(message)
 
    def debug(self, message):
        self.logger.debug(message)
 
    def warning(self, message):
        self.logger.warning(message)
 
    def error(self, message):
        self.logger.error(message)