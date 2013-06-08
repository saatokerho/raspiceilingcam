import os.path
from servos import Servo

# Current settings are for my personal use and serve as an example too.

# List your servos here
# Only servoblaster limits the maximum number of servos
SERVOS = [
    Servo(1, 45, 180), # pan
    Servo(0, 55, 235), # tilt
]

POSITIONS = [
    # ('posname', (servo positions), picrotate)
    ('keittio', (50, 210), 90),
    ('koneet', (48, 147), 0),
    ('eteinen', (110, 210), 90),
    ('telkku', (47, 100), 270)
]

TICKDELAY = 0.1 # in seconds

my_dir = os.path.realpath(os.path.dirname(__file__))
SNAP_EXEC = my_dir + "/../www/snap.sh"
