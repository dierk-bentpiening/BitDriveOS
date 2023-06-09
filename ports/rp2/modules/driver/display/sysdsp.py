from machine import Pin, I2C
from .ssd1306 import SSD1306_I2C

class SysDSP:
    def __init__(self, i2cbus):
        self.framebuffer = [];
        self._i2c = i2cbus;
        self._sys_display = SSD1306_I2C(128, 64, self._i2c);
        self._sys_display.text('', 0, 0, 1);
        self._sys_display.show();
    
    def printf_dsp(self, msg):
        self._sys_display.poweroff();
        self._sys_display.poweron();
        self._sys_display.init_display()
        self._sys_display.text(msg, 0, 0, 1);
        self._sys_display.show();
        
    
        