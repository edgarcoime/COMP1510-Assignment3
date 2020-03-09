"""
Test the max and min of the roll_die function as well as the calculation
"""
from unittest import TestCase
import unittest.mock
import sud


class TestRollDie(TestCase):

    def test_roll_one_sided_die_once(self):
        expected = 1
        actual = sud.roll_die(1, 1)
        self.assertEqual(expected, actual, "Roll 1 sided die once")

    def test_roll_six_sided_die_once(self):
        actual = sud.roll_die(1, 6)
        self.assertGreaterEqual(actual, 1)
        self.assertLessEqual(actual, 6, "Roll 6 sided die once")

    def test_roll_six_sided_die_twice(self):
        actual = sud.roll_die(2, 6)
        self.assertGreaterEqual(actual, 2)
        self.assertLessEqual(actual, 12)

    def test_roll_twenty_sided_die_once(self):
        actual = sud.roll_die(1, 20)
        self.assertGreaterEqual(actual, 1)
        self.assertLessEqual(actual, 20, "Roll 20 sided die once")

    def test_roll_ten_sided_die_ten_times(self):
        actual = sud.roll_die(10, 10)
        self.assertGreaterEqual(actual, 10)
        self.assertLessEqual(actual, 100, "Roll 10 sided die 10 times")

    @unittest.mock.patch('random.randint', side_effect=[3])
    def test_roll_die_single_roll(self, _):
        actual = sud.roll_die(1, 3)
        self.assertEqual(actual, 3, "Test addition, patched 3, expect 3")

    @unittest.mock.patch('random.randint', side_effect=[10, 8])
    def test_roll_die_double_roll(self, _):
        actual = sud.roll_die(2, 8)
        self.assertEqual(actual, 18, "Test addition, patched [10, 8], expect 18")

    @unittest.mock.patch('random.randint', side_effect=[10, 5, 8])
    def test_roll_die_triple_roll(self, _):
        actual = sud.roll_die(3, 10)
        self.assertEqual(actual, 23, "Test addition, patched [10, 5, 8], expect 23")
