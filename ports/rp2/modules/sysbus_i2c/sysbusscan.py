import machine
from _boot import sysbus


class ScanSysB():
    def __init__(self):
        self._devicemap = {}
        
    @property
    def sysdevices(self):
        return self._devicemap
    
    @sysdevices.setter
    def sysdevices(self, value):
        self._devicemap[value] = {"devicename": value}
        
    def scan(self):
        print('Scanning sysbus...')
        devices = sysbus.scan()

        if len(devices) == 0:
            print("No devices on sysbus present !")
        else:
            print('Sysbus Devices found:',len(devices))

        for device in devices:  
            print("Decimal address: ",device," | Hex address: ", hex(device))
            