import os
from  datetime import datetime
from os import path
class SysLogger:
    def __init__(self):
        self.logfile_name = f"/sd/log{datetime.now().strftime('%Y-%m-%d')}.syslog"
        if path.exists(self.logfile_name):
            self.logfile = open(self.logfile_name, "rw")
        else:
            self.logfile = open(self.logfile_name, "w")
            self.logfile.write("Logfile Created")