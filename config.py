import board

# Pin for Stepper Drive Pulses
PUL_pin = board.D12
# Pin for Controller Direction Bit
DIR_pin = board.D11
# Pin for Controller Enable Bit
ENA_pin = board.D10

# This is actualy a delay between PUL pulses
# effectively sets the motor rotation speed.
delay = 0.0000001

# pause due to a possible change direction
pause = .5

# Used for test(). Delete the following if test() not used.
# This is the number of steps that the motor is spinning. 
# Used for forward direction.
stepsFwd = 5000
# This is the number of steps that the motor is spinning. 
# Used for reverse direction.
stepsBwd = 5000
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
    
