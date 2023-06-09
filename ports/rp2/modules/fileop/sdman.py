import os
from machine import Pin, SPI
import machine
from driver.storage import SDCard


class SDMan:
    def __init__(self):
        self._spi0 = SPI(0,
            sck=Pin(2), 
            miso=Pin(0), 
            mosi=Pin(3))
        self._sd = SDCard(self._spi0, Pin(18));
        self._vfs = os.VfsFat(self._sd);
        os.mount(self._vfs, "/sd");
        self._file = None
        
    def load(self, filename):
        try:
            with open(f"/sd/{filename}", "r") as file_operator:
                self._file = file_operator.read()
        except IOError as ex:
            print(f"Error loading")
            exit(1)
        finally:
            return self._file
                