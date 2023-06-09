import gc
from machine import Pin
from utime import sleep_ms
class RamMan:
    def __init__(self):
        gc.collect()
        self._addrreg = Pin(15, Pin.OUT)
        self._addreg_selc = Pin(14, Pin.OUT)
        self._addreg_selc.high()
        
    def reset_progmem(self):
        self._addreg_selc.low()
        sleep_ms(199)
        self._addreg_selc.high()
    
    def free_mem(self, full=True):
        F = gc.mem_free()
        A = gc.mem_alloc()
        T = F+A
        P = '{0:.2f}%'.format(F/T*100)
        if not full: 
            return P
        else: 
            msg = f'T: {int(T/1000)} KB F: {int(F/1000)} KB'
            print(msg)
            return msg
        
    def clr_mem(self):
        F = int(gc.mem_free()) / 1000
        A = int(gc.mem_alloc()) / 1000
        T = int(F+A) / 1000
        ramu_bf = T - F
        gc.collect()
        F = int(gc.mem_free()) / 1000
        ramu_cur = T - F
        clr_mem = ramu_bf - ramu_cur
        msg = f"Cleared {clr_mem} KB Memory!"
        print(msg)
        return msg
        