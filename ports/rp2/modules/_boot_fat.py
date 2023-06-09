import os
import machine, rp2
from machine import SPI, Pin


# Try to mount the filesystem, and format the flash if it doesn't exist.
bdev = rp2.Flash()
try:
    vfs = os.VfsFat(bdev)
    os.mount(vfs, "/")
except:
    os.VfsFat.mkfs(bdev)
    vfs = os.VfsFat(bdev)
os.mount(vfs, "/")

del os, bdev, vfs


spi0 = SPI(0,
            sck=Pin(2), 
            miso=Pin(0), 
            mosi=Pin(3))
sd = SDCard(spi0, Pin(18));
vfs = os.VfsFat(sd);
os.mount(vfs, "/sd");