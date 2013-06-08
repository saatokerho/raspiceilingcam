#!/usr/bin/python

"""Super simple and stupid quick hack to control the servos manually
with the WASD keys or to turn them to a specific position"""

import sys
import tty
import termios

def update(p, t):
    print p, t, "\r"
    open("/dev/servoblaster", "w").write("0=%d\n1=%d\n" % (t, p))

def loop():
    pan = 100
    tilt = 150
    cmds = {"w": (0, 1), "s": (0, -1), "a": (-1, 0), "d": (1, 0)}
    while True:
        ch = sys.stdin.read(1)
        if ord(ch) == 3:
            break
        if ch in cmds:
            pan += cmds[ch][0]
            tilt += cmds[ch][1]
            update(pan, tilt)

def interactive():
    fd = sys.stdin.fileno()
    oldtty = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        loop()
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldtty)

def main():
    if len(sys.argv) != 3:
        interactive()
    else:
        update(int(sys.argv[1]), int(sys.argv[2]))

if __name__ == "__main__":
    main()
