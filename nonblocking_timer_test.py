import unittest
from unittest.mock import patch
import nonblocking_timer


class NonBlockingTimerTestCase(unittest.TestCase):

  @patch('time.monotonic')
  def test_nonblocking_timer(self, monotonic):
    monotonic.return_value = 0
    timer = nonblocking_timer.NonBlockingTimer()
    self.assertIsInstance(timer, nonblocking_timer.NonBlockingTimer)

    with self.assertRaises(Exception):
      timer.set_interval(-1)

    with self.assertRaises(Exception):
      timer.next()

    with self.assertRaises(Exception):
      timer.start()

    timer.set_interval(10)
    self.assertEqual(timer.get_interval(), 10)

    # status is _STOPPED, should not trigger
    with self.assertRaises(Exception):
      timer.next()

    timer.start()
    # time is 0, should not trigger
    self.assertFalse(timer.next())

    monotonic.return_value = 10
    # time is 10, should trigger once
    self.assertTrue(timer.next())
    self.assertFalse(timer.next())

    # time is 15, should not trigger
    monotonic.return_value = 15
    self.assertFalse(timer.next())

    # time is 21, should not trigger
    monotonic.return_value = 21
    self.assertTrue(timer.next())
    self.assertFalse(timer.next())
