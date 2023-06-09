import os

class ConfigPath:
    
    def __init__(self, basepath="/sd/"):
        self._basepath = basepath
        
    def checkcfgpath(self):
        if not os.path.exists(self._basepath):
            return False
        else:
            return True
    

        