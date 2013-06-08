class Servo(object):
    """One servo with an id number for servoblaster and a position.
    
    The minpos and maxpos values are physical safety margins that you should
    determine experimentally.
    """
    def __init__(self, num, minpos, maxpos, pos=None):
        self._num = num
        self._range = (minpos, maxpos)
        self.pos = pos if pos is not None else minpos

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        if value < self._range[0] or value > self._range[1]:
            raise ValueError("Servo value %d out of bounds" % value)
        self._pos = value

    def write(self, fh):
        fh.write("%d=%d\n" % (self._num, self._pos))

class ServoDrive(object):
    """Combine all the servos of one mechanism"""
    def __init__(self, servos, ctrlfile="/dev/servoblaster"):
        self._servos = servos
        self._fh = open(ctrlfile, "w")

    def sync(self):
        for s in self._servos:
            s.write(self._fh)
        self._fh.flush()
