from machine import UART

#
# original code : https://github.com/sensai7/Micropython-midi-library
#

# generic MIDI macros
BAUD = 31250
FREQUENCY = BAUD
 
# MIDI message macros
MESSAGE_CONTROL_CHANGE = 0xB0

class Midi:
    def __init__(self, uart, tx, rx):
        print("Starting MIDI...")
        self.uart = UART(uart, BAUD, tx=tx, rx=rx)

    def write(self, value: int):
        self.uart.write(bytes([value]))

    def send_control_change(self, channel: int, cc: int, value: int):
        self.write(MESSAGE_CONTROL_CHANGE | channel)
        self.write(cc)
        self.write(value)
