.. image:: https://readthedocs.org/projects/circuitpython-nonblocking_timer/badge/?version=latest
    :target: https://circuitpython-nonblocking_timer.readthedocs.io/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://travis-ci.org/mikepschneider/CircuitPython_nonblocking_timer.svg?branch=master
    :target: https://travis-ci.org/mikepschneider/CircuitPython_nonblocking_timer
    :alt: Build Status

Introduction
============

nonblockingtimer is a class to simplify the use of time.monotinic() when working with
CircuitPython. It keeps track of the time interval bookkeeping so you can simply
set a timer (or many), without using time.sleep(), and still respond to events
when your timer(s) is/are sleeping.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
=============

..
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


  
Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/mikepschneider/CircuitPython_nonblocking_timer/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Building locally
================

Zip release files
-----------------

To build this library locally you'll need to install the
`circuitpython-build-tools <https://github.com/adafruit/circuitpython-build-tools>`_ package.

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install circuitpython-build-tools

Once installed, make sure you are in the virtual environment:

.. code-block:: shell

    source .env/bin/activate

Then run the build:

.. code-block:: shell

    circuitpython-build-bundles --filename_prefix circuitpython-nonblocking_timer --library_location .

Sphinx documentation
-----------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass
