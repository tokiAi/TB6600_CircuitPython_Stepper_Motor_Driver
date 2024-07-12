# cathode configuration
# (-)PINs: ENA-, DIR-, PUL- to GND
# (+)PINS: ENA+ to D10, DIR+ to D11, PUL+ to D12
# A+,A-,B+,B- to motor
# GND to power supply GND
# VCC to power supply VCC


import config
import digitalio
from time import sleep


class TB6600:
    
    def __init__(self):
        self.PUL_pin = config.PUL_pin
        self.DIR_pin = config.DIR_pin
        self.ENA_pin = config.ENA_pin
        self.delay = config.delay
        self.pause = config.pause
        
        # delete if test() not used
        self.stepsFwd = config.stepsFwd
        self.stepsBwd = config.stepsBwd
        self.cycles = config.cycles
        self.cyclecount = config.cyclecount

        config.print_config()
        self.PUL = digitalio.DigitalInOut(self.PUL_pin)
        self.DIR = digitalio.DigitalInOut(self.DIR_pin)
        self.ENA = digitalio.DigitalInOut(self.ENA_pin)
        self.PUL.direction = digitalio.Direction.OUTPUT
        self.DIR.direction = digitalio.Direction.OUTPUT
        self.ENA.direction = digitalio.Direction.OUTPUT
        print('Initialization Completed')

    # Enable Controller
    def enable(self):
        self.ENA.value = False
        print('ENA set to LOW - Controller Enabled')

    # Disable Controller
    def disable(self):
        self.ENA.value = True
        print('ENA set to HIGH - Controller Disabled')

    # Moving the motor    
    def move(self, direction, steps, sleep_delay):
        if self.ENA.value:
            raise RuntimeError('Please enable the controller with enable().')
        if self.DIR.value != direction:
            # pause due to a possible change direction
            str_change_direction = ' - due to a change direction.'
            print('Paused for ' + str(sleep_delay) + str_change_direction)
            sleep(sleep_delay)
        self.DIR.value = direction
        if direction:
            print('DIR set to HIGH - Moving Backward at ' + str(self.delay))
        else:
            print('DIR set to LOW - Moving Forward at ' + str(self.delay))
        print('Controller PUL being driven.')
        for x in range(steps):
            print(f"steps: {x} / {steps}")  # do not remove on: RP Pico circuitpython 9.0.5. (bugfix)
            self.PUL.value = not self.PUL.value
            sleep(self.delay)

    def forward(self, steps, sleep_delay=.5):
        self.move(False, steps, sleep_delay)

    def reverse(self, steps, sleep_delay=.5):
        self.move(True, steps, sleep_delay)

    # if not used can be deleted.
    def test(self):
        while self.cyclecount < self.cycles:
            print('Number of cycles completed: ' + str(self.cyclecount))
            str_cycles_remaining = 'Number of cycles remaining: '
            print(str_cycles_remaining + str(self.cycles - self.cyclecount))
            self.enable()
            self.forward(self.stepsFwd, self.pause)
            self.reverse(self.stepsBwd, self.pause)
            self.cyclecount = (self.cyclecount + 1)
            self.disable()
        self.cyclecount = config.cyclecount
        print('Cycling Completed')


# execution example with test()
driver = TB6600()
driver.test()
