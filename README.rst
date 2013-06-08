Raspberry Pi ceiling camera server
==================================

This small tool rotates `RC servos`_ (using the ServoBlaster_ driver)
constantly to predetermined positions and takes pictures with the camera board
(using the raspistill tool) that is assumed to be attached to the servos. The
latest pictures are stored in a ramdisk to reduce SD card wear.

.. _RC servos: http://en.wikipedia.org/wiki/Servo_(radio_control)
.. _ServoBlaster: https://github.com/richardghirst/PiBits

The Pi just serves the most current images, and it's accessed via a proxy in
another server. The other server also periodically pulls the pics and archives
them. I'm using lighttpd_ on the Pi.

.. _lighttpd: http://www.lighttpd.net/

This is used in the guild room of Aalto university's `guild of automation and
systems technology`_. See also `my blog post`_ (in Finnish).

.. _guild of automation and systems technology: http://as.ayy.fi/
.. _my blog post: http://sooda.dy.fi/2013/6/8/raspi-kattokamera/


Usage
-----

Make sure the image directory exists, and publish it::

  sudo www/mount.sh
  ln -s `pwd`/www/cam /var/www/

Don't forget to remount after boot (if you ever do that). A line in fstab is
fine too. Also, /run seems to be a tmpfs on RPi, so you could use that instead.

Rotate the servos manually while watching the jpg file change in a browser, and
record the positions you want to use::

  sh www/snaploop.sh &
  servoctl/manual.py
  kill %1
  $EDITOR servoctl/settings.py

Finally, run the drive.py script to check that it's working::

  servoctl/drive.py

It's not a daemon process, but you can leave it running in screen or use
nohup::

  nohup servoctl/drive.py > /dev/null &


TODO
----

A lot.


License
-------

WTFPL_.

.. _WTFPL: http://www.wtfpl.net/
