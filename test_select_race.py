"""
Test select_race.
"""
from unittest import TestCase

import unittest.mock
import sud


class TestSelectRace(TestCase):
    @unittest.mock.patch('builtins.input', side_effect=[1])
    def test_select_race_1(self, _):
        """Test output when user input is 1"""

        actual = sud.select_race()
        expected = 'dwarf'
        self.assertEqual(actual, expected, "User input is 1")

    @unittest.mock.patch('builtins.input', side_effect=[3])
    def test_select_race_3(self, _):
        """Test output when user input is 3"""

        actual = sud.select_race()
        expected = 'halfling'
        self.assertEqual(actual, expected, "User input is 3")

    @unittest.mock.patch('builtins.input', side_effect=[6])
    def test_select_race_6(self, _):
        """Test output when user input is 6"""

        actual = sud.select_race()
        expected = 'gnome'
        self.assertEqual(actual, expected, "User input is 6")

    @unittest.mock.patch('builtins.input', side_effect=[9])
    def test_select_race_9(self, _):
        """Test output when user input is 9"""

        actual = sud.select_race()
        expected = 'tiefling'
        self.assertEqual(actual, expected, "User input is 9")
