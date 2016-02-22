#! /usr/bin/env python3

from bowling_calc import score
import unittest

class BowlingTests(unittest.TestCase):
  def test_strikes(self):
    self.assertEqual(score('XXXXXXXXXXXX'), 300)
  def test_scores(self):
    self.assertEqual(score('9-9-9-9-9-9-9-9-9-9-'), 90)
  def test_spares(self):
    self.assertEqual(score('5/5/5/5/5/5/5/5/5/5/5'), 150)
  def test_no_extra_point(self):
    self.assertEqual(score('5/------------------'), 10)
  def test_nearly_all_strikes(self):
    self.assertEqual(score('XXXXXXXXXX--'), 270)

if __name__ == '__main__':
  unittest.main()
