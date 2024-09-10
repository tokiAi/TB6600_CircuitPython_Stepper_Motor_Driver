# TB6600_CircuitPython_Stepper_Motor_Driver
A Stepper Motor Driver for TB6600 in CircuitPython

The code was inspired by
https://www.instructables.com/Raspberry-Pi-Python-and-a-TB6600-Stepper-Motor-Dri/
and can be use as a base for the implementation of TB6600 Driver (or for wiring testing).

## Cathode configuration
- (-)PINs: 
  - ENA-, DIR-, PUL- to GND
- (+)PINS: 
  - ENA+ to D10 
  - DIR+ to D11
  - PUL+ to D12
- A+,A-,B+,B- to motor
- GND to power supply GND
- VCC to power supply VCC

## Start with code.py
"CircuitPython looks for a code file on the board to run. There are four options: **code.txt**, **code.py**, **main.txt** and **main.py**. CircuitPython looks for those files, in that order, and then runs the first one it finds. While **code.py** is the recommended name for your code file, it is important to know that the other options exist. If your program doesn't seem to be updating as you work, make sure you haven't created another code file that's being read instead of the one you're working on." from https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code

## Configuration dependent on the controller
You need to adjust the `delay` in `config.py` based on the controller you're using. For example:

- **Nvidia Jetson TX2**: Set the delay to `0.0000001`.
- **Raspberry Pi Pico (v1)**: Set the delay to `0.001`.

If you use `0.0000001` on the Pico, you may hear a change in the motor sound, but no movement will occur.
