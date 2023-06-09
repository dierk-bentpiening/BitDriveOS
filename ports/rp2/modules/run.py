import os
import time
from machine import Pin, SPI

import microdot
internal_led = Pin("LED", Pin.OUT);
internal_led.on();

from _boot import ram, storage, sound

from driver.sound import SoundSubSystem;
from ramrom import RamMan
sound_drv = SoundSubSystem();
mem = RamMan()

