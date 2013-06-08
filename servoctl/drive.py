#!/usr/bin/python

"""Loop forever, going through the servo position list, and take a picture at
every position"""

from servos import Servo, ServoDrive
import settings
import subprocess
import time

def go(servos, targets, drive):
    """Rotate the servos to target positions slowly"""
    pairs = zip(servos, targets)
    while any([servo.pos != target for servo, target in pairs]):
        for servo, target in pairs:
            if servo.pos < target:
                servo.pos += 1
            elif servo.pos > target:
                servo.pos -= 1
        drive.sync()
        time.sleep(settings.TICKDELAY)

def main():
    """Iterate the positions"""
    servos = settings.SERVOS
    drive = ServoDrive(servos)
    while True:
        for pos in settings.POSITIONS:
            print pos[0]
            go(servos, pos[1], drive)
            subprocess.call([settings.SNAP_EXEC, pos[0], str(pos[2])])

if __name__ == "__main__":
    main()
