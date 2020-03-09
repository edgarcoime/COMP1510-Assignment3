"""
Test select_class.
"""
from unittest import TestCase

import unittest.mock
import sud


class TestSelectClass(TestCase):
    @unittest.mock.patch('builtins.input', side_effect=[1])
    def test_select_class_1(self, _):
        """Test output when user input is 1"""

        actual = sud.select_class()
        expected = "barbarian"
        self.assertEqual(actual, expected, "User input is 1")

    @unittest.mock.patch('builtins.input', side_effect=[4])
    def test_select_class_4(self, _):
        """Test output when user input is 4"""

        actual = sud.select_class()
        expected = "druid"
        self.assertEqual(actual, expected, "User input is 4")

    @unittest.mock.patch('builtins.input', side_effect=[8])
    def test_select_class_8(self, _):
        """Test output when user input is 8"""

        actual = sud.select_class()
        expected = "ranger"
        self.assertEqual(actual, expected, "User input is 8")

    @unittest.mock.patch('builtins.input', side_effect=[12])
    def test_select_class_12(self, _):
        """Test output when user input is 12"""

        actual = sud.select_class()
        expected = "wizard"
        self.assertEqual(actual, expected, "User input is 12")
