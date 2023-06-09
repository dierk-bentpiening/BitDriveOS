import os
import machine, rp2
from machine import SPI, Pin, SoftI2C
from driver.storage import SDCard
from driver.display.lcd_i2c import LCD

from ramrom import RamMan
from fileop import SDMan
from driver.sound import SoundSubSystem
storage = SDMan()
ram = RamMan()
I2C_ADDR = 0x27
NUM_ROWS = 4
NUM_COLS = 20
i2c = SoftI2C(scl=Pin(17), sda=Pin(16), freq=800_000)
lcd = LCD(addr=I2C_ADDR, cols=NUM_COLS, rows=NUM_ROWS, i2c=i2c)
lcd.begin()
lcd.set_cursor(row=0, col=0)
lcd.print("BDOS v1.0")
lcd.set_cursor(row=1, col=0)
lcd.print(ram.free_mem())
lcd.set_cursor(row=2, col=0)
lcd.print("READY...")
lcd.blink()

# Try to mount the filesystem, and format the flash if it doesn't exist.
# Note: the flash requires the programming size to be aligned to 256 bytes.
bdev = rp2.Flash();
try:
    vfs = os.VfsLfs2(bdev, progsize=256);
    os.mount(vfs, "/");
except:
    os.VfsLfs2.mkfs(bdev, progsize=256);
    vfs = os.VfsLfs2(bdev, progsize=256);

    
del os, bdev, vfs

spi0 = SPI(0,
            sck=Pin(2), 
            miso=Pin(0), 
            mosi=Pin(3))
sd = SDCard(spi0, Pin(18));
vfs = os.VfsFat(sd);
os.mount(vfs, "/sd");
sound = SoundSubSystem()

