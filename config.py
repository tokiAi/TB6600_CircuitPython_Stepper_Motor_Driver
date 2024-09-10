import board

# Pins are board.D.. for Nvidia Jetson.
# Pins are board.GP.. for Raspberry Pi Pico.

# Pin for Stepper Drive Pulses
PUL_pin = board.D12
# Pin for Controller Direction Bit
DIR_pin = board.D11
# Pin for Controller Enable Bit
ENA_pin = board.D10

# This is actualy a delay between PUL pulses
# effectively sets the motor rotation speed.
# Configuration of delay dependent on the controller
# e.g Nvidia Jetson TX2 = 0.0000001
# e.g Raspberry Pi Pico (v1) = 0.001
delay = 0.0000001

# pause due to a possible change direction
pause = .5

# Used for test(). Delete the following if test() not used.
# This is the number of steps that the motor is spinning. 
# Used for forward direction.
# At 1.8 degrees per step, 200 steps make a full rotation of the stepper motor.
stepsFwd = 200
# This is the number of steps that the motor is spinning. 
# Used for reverse direction.
# At 1.8 degrees per step, 200 steps make a full rotation of the stepper motor.
stepsBwd = 200
# This is the number of cycles to be run once program is started.
cycles = 1000
# This is the iteration of cycles to be run once program is started.
cyclecount = 0


def print_config():
    print('PUL = GPIO {}'.format(PUL_pin).replace('board.', ''))
    print('DIR = GPIO {}'.format(DIR_pin).replace('board.', ''))
    print('ENA = GPIO {}'.format(ENA_pin).replace('board.', ''))
    print('Speed set to ' + str(delay))
    print('Pause due to a possible change direction set to ' + str(pause))

    # Used for test(). Delete the following if test() not used.
    print('Duration Fwd set to ' + str(stepsFwd))
    print('Duration Bwd set to ' + str(stepsBwd))
    print('number of Cycles to Run set to ' + str(cycles))
    
