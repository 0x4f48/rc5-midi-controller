# BOSS RC-5 MIDI Controller


## Readme

The default drum level of the RC-5 is 100, and it is too loud. Although you can adjust it in its menu, it takes multiple button pressing and knob turning. If you have used an older model like RC-3, the adjustment is as simple as just turning a knob. Since the RC-5 supports MIDI control, I decided to make a single knob drum level controller.

![RC5 MIDI controller](https://github.com/0x4f48/rc5-midi-controller/blob/main/misc/rc5-midi-controller.jpg)

![RC5 MIDI controller2](https://github.com/0x4f48/rc5-midi-controller/blob/main/misc/rc5-midi-controller2.jpg)

It is a simple function device, and I don't want to spend too much time to build it. This thought brought me followings.

	• Use MicroPython for quick software development.
	• Use existing modules to avoid custom PCB fabrication.
	• Use parts in my hands.


### Parts

	• I2C OLED display (128x64) x 1
	• DC-DC module (9V to 5V) x 1
	• ESP32 module x 1
	• KY-040 rotary encode x 1
	• Power jack x 2
	• 3.5mm stereo jack x 2
    • 220 ohm resistor x 1


### Installing Software

	• Install MicroPython firmware (https://micropython.org/download/ESP32_GENERIC/) to a ESP dev kit board.
	• Copy python files into the board. (https://www.pythontutorials.net/blog/micropython-rshell/)


### Building Controller

I designed 3D models quickly and assemble the parts in it.

	• See 3D model directory.


Check the schematics to assemble the parts.

    • Input power lines (9V) is directly hooked up to the output jack for RC-5.




### Using Controller

	• In the RC-5 setup menu set MIDI CC #80 and #81 as below.
		○ CC #80: DRUM LEVEL2
		○ CC #81: TRACK LEVEL 2
	• Controller sends initial drum level, which is 50,  as soon as it boots up.
		○ Turning the encoder will increase or decrease drum/track level.
		○ Pushing the encoder will switch its mode to track level mode. Default track level is 100.

