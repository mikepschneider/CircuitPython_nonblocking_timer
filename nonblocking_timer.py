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

.. todo:: Describe what the module does

* Author(s): Michael Schneider
"""

# imports

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/mikepschneider/CircuitPython_nonblocking_timer.git"


import time

class NonBlockingTimer:
    _STOPPED = 0
    _RUNNING = 1

    def __init__(self, interval = -1):
        """Create a new timer with optional interval. Initial state is STOPPED.
           Call start() to set status to RUNNING. """
        self._interval = interval
        self._status = NonBlockingTimer._STOPPED
        self._start_time = 0

    def next(self):
        """ Returns true or false according to the following algorithm:

            if status == STOPPED return False
            if time.monotic() - start_time > interval return True
            else return False
        """

        if self._status != NonBlockingTimer.RUNNING:
            return False

        current_time = time.monotonic()
        elapsed = current_time - self._start_time

        if (elapsed > self._interval):
            # The timer has been "triggered"
            self._start_time = current_time
            return True
        return False

    def stop(self):
        """Sets status to STOPPED. Do any cleanup here such as releasing pins,
           etc. Call start() to restart."""
        self._status = NonBlockingTimer.STOPPED

    def start(self):
        """Sets status to RUNNING. Sets start_time to time.monontic(). Call
           next() repeatedly to determine if the timer has been triggered. """
        self._start_time = time.monotonic()
        self._status = NonBlockingTimer.RUNNING

    def set_interval(self, seconds):
        """ Set the trigger interval time in seconds (float). If seconds <= 0,
            will raise an exception. """
        self._interval = seconds
