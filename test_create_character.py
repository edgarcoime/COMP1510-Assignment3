"""
test create character function to make sure it produces a valid character dictionary.
"""
from unittest import TestCase

import unittest.mock
import io
import sud


class TestCreateCharacter(TestCase):

    @unittest.mock.patch('sud.select_class', side_effect=["bard"])
    @unittest.mock.patch('sud.select_race', side_effect=["dwarf"])
    @unittest.mock.patch('builtins.input', side_effect=['Edgar'])
    def test_create_character_valid_input(self, _, __, ___):
        expected_dictionary = {
            'Name': 'Edgar',
            'Class': 'bard',
            'Race': 'dwarf',
            'HP': [20, 20],
            'current_location': (3, 3)
        }
        actual = sud.create_character()
        self.assertEqual(actual, expected_dictionary, "Input is valid and generates a user's in game character.")

