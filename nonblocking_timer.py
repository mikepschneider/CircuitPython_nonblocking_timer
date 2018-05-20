# The MIT License (MIT)
#
# Copyright (c) 2017 Michael Schneider
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`nonblocking_timer`
====================================================

.. This class allows easier usage of time.monotonic() to keep track of timers
   without using time.sleep().

   Example:


class BlinkDemo(NonBlockingTimer):
    def __init__(self):
        super(BlinkDemo, self).__init__(0.1)
        self.led = digitalio.DigitalInOut(board.D13)
        self.led.direction = digitalio.Direction.OUTPUT
        self.value = True

    def stop(self):
        self.led.value = False

    def next(self):
        if (super(BlinkDemo, self).next()):
            self.led.value = not (self.led.value)

blinkdemo.BlinkDemo()

while True:
  blinkDemo.next()
  # This is the only place you should use time.sleep: to set the overall
  # "sampling rate" of your program.
  time.sleep(0.001)

* Author(s): Michael Schneider
"""

# imports

__version__ = "0.0.0-auto.0"
__repo__ = \
  "https://github.com/mikepschneider/CircuitPython_nonblocking_timer.git"


import time

class NonBlockingTimer(object):
  """ Non blocking timer class for use with CircuitPython """
  _STOPPED = 0
  _RUNNING = 1

  def __init__(self, interval=-1):
    """Create a new timer with optional interval. Initial state is _STOPPED.
       Call start() to set status to _RUNNING. """
    self._interval = interval
    self._status = NonBlockingTimer._STOPPED
    self._start_time = 0

  def next(self):
    """ Returns true or false according to the following algorithm:

      if status == _STOPPED return False
      if time.monotonic() - start_time > interval return True
      else return False
    """

    if self._status != NonBlockingTimer._RUNNING:
      return False

    current_time = time.monotonic()
    elapsed = current_time - self._start_time

    if elapsed > self._interval:
      # The timer has been "triggered"
      self._start_time = current_time
      return True
    return False

  def stop(self):
    """Sets status to _STOPPED. Do any cleanup here such as releasing pins,
       etc. Call start() to restart."""
    self._status = NonBlockingTimer._STOPPED

  def start(self):
    """Sets status to _RUNNING. Sets start_time to time.monotonic(). Call
       next() repeatedly to determine if the timer has been triggered. """
    self._start_time = time.monotonic()
    self._status = NonBlockingTimer._RUNNING

  def set_interval(self, seconds):
    """ Set the trigger interval time in seconds (float). If seconds <= 0,
        will raise an exception. """
    self._interval = seconds
