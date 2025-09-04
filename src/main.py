from machine import Pin, I2C
from rotary import Rotary
import time
import ssd1306
from levelctrl import LevelCtrl
import midi

level = LevelCtrl()
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
rotary = Rotary(26,27,25)

oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

MIDI_TX = Pin(17)
MIDI_RX = Pin(16)

midi_io = midi.Midi(2, tx=MIDI_TX, rx=MIDI_RX)
midi_channel= 0
midi_drum_cc = 80
midi_track_cc = 81

def oled_text_scaled(oled, text, x, y, scale, character_width=8, character_height=8):
    # temporary buffer for the text
    width = character_width * len(text)
    height = character_height
    temp_buf = bytearray(width * height)
    temp_fb = ssd1306.framebuf.FrameBuffer(temp_buf, width, height, ssd1306.framebuf.MONO_VLSB)

    # write text to the temporary framebuffer
    temp_fb.text(text, 0, 0, 1)

    # scale and write to the display
    for i in range(width):
        for j in range(height):
            pixel = temp_fb.pixel(i, j)
            if pixel:  # If the pixel is set, draw a larger rectangle
                oled.fill_rect(x + i * scale, y + j * scale, scale, scale, 1)

def redraw(oled, level_ctrl):
    oled.fill(0)
    val = level_ctrl.curr_level()
    if level_ctrl.curr_mode() is level_ctrl.DRUM:
        oled_text_scaled(oled, f'DRM:{val}', 5, 12, 2)
        midi_io.send_control_change(midi_channel, midi_drum_cc, val)
    else :
        oled_text_scaled(oled, f'TRK:{val}', 5, 12, 2)
        midi_io.send_control_change(midi_channel, midi_track_cc, val)
    oled.show()

def rotary_changed(change):
    global oled, level
    if change == Rotary.ROT_CW:
        #print('CW')
        level.increase()
        redraw(oled, level)
    elif change == Rotary.ROT_CCW:
        #print('CCW')
        level.decrease()
        redraw(oled, level)
    #elif change == Rotary.SW_PRESS:
    #    print('PRESS')
    elif change == Rotary.SW_RELEASE:
        #print('REL')
        level.toggle_mode()
        redraw(oled, level)

rotary.add_handler(rotary_changed)
redraw(oled, level)



while True:
    time.sleep(1)
