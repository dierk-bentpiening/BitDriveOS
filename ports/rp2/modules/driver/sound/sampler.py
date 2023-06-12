import os
from machine import Pin, PWM, SoftI2C
from utime import sleep, sleep_ms
from driver.display.lcd_i2c import LCD
from machine import SoftI2C,
from math import log2, pow
from random import randint

I2C_ADDR = 0x27
NUM_ROWS = 4
NUM_COLS = 20

class SoundSubSystem():
    def __init__(self):
        self.i2c = SoftI2C(scl=Pin(17), sda=Pin(16), freq=800_000)
        self.lcd = LCD(addr=I2C_ADDR, cols=NUM_COLS, rows=NUM_ROWS, i2c=self.i2c)

        self.lcd.begin()
        self.lcd.set_cursor(row=0, col=0)
        self.lcd.print("BitDrive Synth")
        self.paudio_channel_0 = PWM(Pin(9)) 
        self.paudio_channel_1 = PWM(Pin(8))
        self.paudio_channel_2 = PWM(Pin(7))
        self.paudio_channel_3 = PWM(Pin(6))
        self.paudio_channel_4 = PWM(Pin(21))
        self._channels = [self.paudio_channel_0, self.paudio_channel_1, self.paudio_channel_2, self.paudio_channel_3, self.paudio_channel_4]
        self.stop_all()

        self.tones = {
            "C0": 16.35,
            "C#0/Db0": 17.32,
            "D0": 18.35,
            "D#0/Eb0": 19.45,
            "E0": 20.60,
            "F0": 21.83,
            "F#0/Gb0": 23.12,
            "G0": 24.50,
            "G#0/Ab0": 25.96,
            "A0": 27.50,
            "A#0/Bb0": 29.14,
            "B0": 30.87,
            "C1": 32.70,
            "C#1/Db1": 34.65,
            "D1": 36.71,
            "D#1/Eb1": 38.89,
            "E1": 41.20,
            "F1": 43.65,
            "F#1/Gb1": 46.25,
            "G1": 49.00,
            "G#1/Ab1": 51.91,
            "A1": 55.00,
            "A#1/Bb1": 58.27,
            "B1": 61.74,
            "C2": 65.41,
            "C#2/Db2": 69.30,
            "D2": 73.42,
            "D#2/Eb2": 77.78,
            "E2": 82.41,
            "F2": 87.31,
            "F#2/Gb2": 92.50,
            "G2": 98.00,
            "G#2/Ab2": 103.83,
            "A2": 110.00,
            "A#2/Bb2": 116.54,
            "B2": 123.47,
            "C3": 130.81,
            "C#3/Db3": 138.59,
            "D3": 146.83,
            "D#3/Eb3": 155.56,
            "E3": 164.81,
            "F3": 174.61,
            "F#3/Gb3": 185.00,
            "G3": 196.00,
            "G#3/Ab3": 207.65,
            "A3": 220.00,
            "A#3/Bb3": 233.08,
            "B3": 246.94,
            "C4": 261.63,
            "C#4/Db4": 277.18,
            "D4": 293.66,
            "D#4/Eb4": 311.13,
            "E4": 329.63,
            "F4": 349.23,
            "F#4/Gb4": 369.99,
            "G4": 392.00,
            "G#4/Ab4": 415.30,
            "A4": 440.00,
            "A#4/Bb4": 466.16,
            "B4": 493.88,
            "C5": 523.25,
            "C#5/Db5": 554.37,
            "D5": 587.33,
            "D#5/Eb5": 622.25,
            "E5": 659.25,
            "F5": 698.46,
            "F#5/Gb5": 739.99,
            "G5": 783.99,
            "G#5/Ab5": 830.61,
            "A5": 880.00,
            "A#5/Bb5": 932.33,
            "B5": 987.77,
            "C6": 1046.50,
            "C#6/Db6": 1108.73,
            "D6": 1174.66,
            "D#6/Eb6": 1244.51,
            "E6": 1318.51,
            "F6": 1396.91,
            "F#6/Gb6": 1479.98,
            "G6": 1567.98,
            "G#6/Ab6": 1661.22,
            "A6": 1760.00,
            "A#6/Bb6": 1864.66,
            "B6": 1975.53,
            "C7": 2093.00,
            "C#7/Db7": 2217.46,
            "D7": 2349.32,
            "D#7/Eb7": 2489.02,
            "E7": 2637.02,
            "F7": 2793.83,
            "F#7/Gb7": 2959.96,
            "G7": 3135.96,
            "G#7/Ab7": 3322.44,
            "A7": 3520.00,
            "A#7/Bb7": 3729.31,
            "B7": 3951.07,
            "C8": 4186.01,
            "C#8/Db8": 4434.92,
            "D8": 4698.64,
            "D#8/Eb8": 4978.03,
            "E8": 5274.04,
            "F8": 5587.65,
            "F#8/Gb8": 5919.91,
            "G8": 6271.93,
            "G#8/Ab8": 6644.88,
            "A8": 7040.00,
            "A#8/Bb8": 7458.62,
            "B8": 7902.13,
            "A": 440,
            "A#": 466,
            "Bb": 466,
            "B": 44,
            "C": 523,
            "C#": 554,
            "Db": 554,
            "D": 587,
            "D#": 622,
            "Eb": 622,
            "E": 659,
            "F": 698,
            "F#": 740,
            "Gb": 740,
            "G": 784,
            "G#": 831,
            "Ab": 831,
            "-": 000,
        };
    def stop_all(self):
        for chanel in self._channels:
            chanel.duty_u16(0)
    def play_sample(self, notes, temp):
        self.paudio_channel_0.freq(10512);
        self.paudio_channel_0.duty_u16(10512);
        self.paudio_channel_1.freq(100);
        self.paudio_channel_1.duty_u16(10512);
        self.paudio_channel_2.freq(1523);
        self.paudio_channel_2.duty_u16(10512);
        self.paudio_channel_3.freq(131);
        self.paudio_channel_3.duty_u16(10512);
        tempo = 1.0
        for tone in notes:
            self.lcd.set_cursor(col=0, row=1);
            self.lcd.print(f"Tone: [{tone[0]}] length:{tone[1]}");
            self.lcd.set_cursor(row=2, col=0);
            self.lcd.print(f"freq({self.tones[tone[0]]})");
            if(tone[0] == "-"):
                sleep(tone[1]);
            else:
                self.paudio_channel_0.freq(round(self.tones[tone[0]]));
                self.paudio_channel_1.freq(round(self.tones[tone[0]] - 1));
                self.paudio_channel_2.freq(round(self.tones[tone[0]] + 1));
                sleep(tone[1])
        for channel in self._channels:
            channel.duty_u16(0)
    def startsound(self):
        startsound_notes = [
            ("A4", 0.1),
            ("-", 0.1),
            ("A4", 0.1),
            ("-", 0.1),
            ("A4", 0.1),
            ("-", 0.1),
            ("A4", 0.1),
            ("B4", 0.3),
            ("A4", 0.3),
            ("E4", 0.1),
            ("E4", 0.1),
            ("E4", 0.1),
            ("E4", 0.1),
            ("F4", 0.2),
            ("E4", 0.2),
            ("E4", 0,2),
            ("G4", 0.4),
            ("E4", 0.2),
            ("A4", 0.2),
            ("G4", 0.4)
        ];
        self.play_sample(startsound_notes, 1);


    def _pitch(self, freq):
        return (2**((freq-69)/12))*440

    def _duty_cycle(self, percent):
        return round((percent/100)*65535)

    def play_note(self, note, channel, duty):
        if channel == "a0":
            self.paudio_channel_4.duty_u16(round(self._duty_cycle(duty + 20)))
            self.paudio_channel_4.freq(round(self._pitch(note + 20)))
            self.paudio_channel_0.freq(round(self._pitch(note)))
            self.paudio_channel_0.duty_u16(self._duty_cycle(duty))
            self.paudio_channel_4.duty_u16(round(self._duty_cycle(duty - 15)))
            self.paudio_channel_4.freq(round(self._pitch(note - 40)))

        elif channel == "a1":
            self.paudio_channel_4.duty_u16(round(self._duty_cycle(duty + 20)))
            self.paudio_channel_4.freq(round(self._pitch(note + 20)))
            self.paudio_channel_1.freq(round(self._pitch(note)))
            self.paudio_channel_1.duty_u16(self._duty_cycle(duty))
            self.paudio_channel_4.freq(round(self._pitch(note - 40)))
            self.paudio_channel_4.duty_u16(round(self._duty_cycle(duty - 15)))

        elif channel == "b0":
            self.paudio_channel_4.duty_u16(round(self._duty_cycle(duty + 20)))
            self.paudio_channel_4.freq(round(self._pitch(note + 20)))
            self.paudio_channel_2.freq(round(self._pitch(note)))
            self.paudio_channel_2.duty_u16(self._duty_cycle(duty))
            self.paudio_channel_4.freq(round(self._pitch(note - 40)))
            self.paudio_channel_4.duty_u16(round(self._duty_cycle(duty - 15)))

        elif channel == "b1":
            self.paudio_channel_4.duty_u16(round(self._duty_cycle(duty + 20)))
            self.paudio_channel_4.freq(round(self._pitch(note + 20)))
            self.paudio_channel_3.freq(round(self._pitch(note)))
            self.paudio_channel_3.duty_u16(self._duty_cycle(duty))
            self.paudio_channel_4.freq(round(self._pitch(note - 40)))
            self.paudio_channel_4.duty_u16(round(self._duty_cycle(duty - 15)))

    def stop_channel(self, channel):
        if channel == "a0":
            self.paudio_channel_0.duty_u16(0)
            self.paudio_channel_4.duty_u16(self._duty_cycle(0))
        elif channel == "a1":
            self.paudio_channel_1.duty_u16(0)
            self.paudio_channel_4.duty_u16(self._duty_cycle(0))
        elif channel == "b0":
            self.paudio_channel_2.duty_u16(0)
            self.paudio_channel_4.duty_u16(self._duty_cycle(0))
        elif channel == "b1":
            self.paudio_channel_3.duty_u16(0)

    
    def _opcodes(self):
        return [0x90, 0x91, 0x92, 0x93, 0x80, 0x81, 0x82, 0x83, 0xf0, 0xe0]
    
    def _play_note_opcodes(self):
        return [0x90, 0x91, 0x92, 0x93]

    def _stop_note_opcodes(self):
        return [0x80, 0x81, 0x82, 0x83]
    
    def _end_song_opcodes(self):
        return [0xf0, 0xe0]
    
    def play_song(self, music):
        if type(music) == list:
            done = False
            tmp = []
            index = 0
            isReading = False
            opcode = 0x00
            
            self.stop_all() # Silence any existing music
            sleep(1)
            
            while not done:
                if index >= len(music):
                    print("out of range while reading opcode")
                    done = True
                    break
                else:
                    # Read opcode
                    if music[index] in self._opcodes():
                        opcode = music[index]
                        
                        # Scan for timing data
                        isReading = True
                        tmp = []
                        tmp_index = 1
                        
                        # Read next bytes for timing info
                        while isReading: 
                            if (index + tmp_index) >= len(music):
                                done = True
                                break
                            else:
                                if not music[index + tmp_index] in self._opcodes():
                                    tmp.append(music[index + tmp_index])
                                    tmp_index += 1
                                else:
                                    isReading = False
                        
                        # Execute instruction
                        if opcode in self._play_note_opcodes():
                            # Play voice and goto next instruction or play and wait for x milliseconds
                            if len(tmp) > 0:
                                if opcode == 0x90:
                                    self.play_note(tmp[0], "a0", 50)
                                elif opcode == 0x91:
                                    self.play_note(tmp[0], "b0", 50)
                                elif opcode == 0x92:
                                    self.play_note(tmp[0], "a1", 50)
                                elif opcode == 0x93:
                                    self.play_note(tmp[0], "b1", 50)
                                
                                if len(tmp) == 3:
                                    delay = ((tmp[1]*256)+(tmp[2]))
                                    sleep_ms(delay)
                            index += 1
                            
                        elif opcode in self._stop_note_opcodes():
                            # Mute voice or mute and wait for x milliseconds
                            if opcode == 0x80:
                                self.stop_channel("a0")
                            elif opcode == 0x81:
                                self.stop_channel("b0")
                            elif opcode == 0x82:
                                self.stop_channel("a1")
                            elif opcode == 0x83:
                                self.stop_channel("b1")
                                
                            if len(tmp) >= 2:
                                delay = ((tmp[0]*256)+(tmp[1]))
                                sleep_ms(delay)
                            index += 1
                            
                        elif opcode in self._end_song_opcodes():
                            # End or loop the song
                            if opcode == 0xf0: # Song is over, stop playing.
                                done = True
                                break
                            else:
                                done = False
                                index = 0 # Song is looping, go back to beginning of song.
                    else:
                        index += 1
    @micropython.native
    def play_samplefile(self, path):
        filestring = None
        if (os.path.isfile(path) == True):
            with open(path, 'r') as midi_reader:
                filestring = midi_reader.read();
            
            try:
                sample_notes = filestring.split(",");
            except Exception as ex:
                print(f"Guru Meditation: An error occurred while parsing sample fil\nCause: {str(ex)}")
            else:
                self.play_song(sample_notes);
            
        else:
            raise FileNotFoundError;
            exit(1)
