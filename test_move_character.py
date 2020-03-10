"""
test move character function that determines the new tuple of the desired character location based on the direction.
"""
from unittest import TestCase

import unittest.mock
import io
import sud


class TestMoveCharacter(TestCase):

    @unittest.mock.patch('builtins.input', side_effect=['qut', '   quit'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_move_character_invalid_input_then_quit_input(self, mock_stdout, _):
        my_character = {
            'Name': 'jason',
            'HP': [15, 15],
            'current_location': (1, 5)
        }

        expected_print = "That's not a valid input\n"
        expected_new_location = (1, 5)  # should not modify anything
        expected_return = 'q'
        actual = sud.move_character(my_character)
        self.assertEqual(mock_stdout.getvalue(), expected_print, "Patched user input was first typed 'qut' then 'quit")
        self.assertEqual(actual, expected_return, "Patched user input was first typed 'qut' then 'quit'")
        self.assertTrue(my_character['current_location'] == expected_new_location)

    @unittest.mock.patch('builtins.input', side_effect=['w'])
    def test_move_character_w_for_north(self, _):
        my_character = {
            'Name': 'jason',
            'HP': [15, 15],
            'current_location': (3, 3)
        }

        expected_new_location = (3, 2)  # Northern direction means incrementing down y b/c first row is row 1
        actual = sud.move_character(my_character)
        self.assertTrue(my_character['current_location'] == expected_new_location,
                        "Patched user input typed 'w' for North direction.")

    @unittest.mock.patch('builtins.input', side_effect=['s'])
    def test_move_character_s_for_south(self, _):
        my_character = {
            'Name': 'jason',
            'HP': [15, 15],
            'current_location': (3, 3)
        }

        expected_new_location = (3, 4)  # Southern direction means incrementing up y b/c last/5th row is row 5
        actual = sud.move_character(my_character)
        self.assertTrue(my_character['current_location'] == expected_new_location,
                        "Patched user input typed 's' for South direction.")

    @unittest.mock.patch('builtins.input', side_effect=['a'])
    def test_move_character_a_for_east(self, _):
        my_character = {
            'Name': 'jason',
            'HP': [15, 15],
            'current_location': (3, 3)
        }

        expected_new_location = (2, 3)  # Eastern direction means incrementing down x b/c first column is column 1
        actual = sud.move_character(my_character)
        self.assertTrue(my_character['current_location'] == expected_new_location,
                        "Patched user input typed 'a' for East direction.")

    @unittest.mock.patch('builtins.input', side_effect=['d'])
    def test_move_character_d_for_west(self, _):
        my_character = {
            'Name': 'jason',
            'HP': [15, 15],
            'current_location': (3, 3)
        }

        expected_new_location = (4, 3)  # Eastern direction means incrementing down x b/c first column is column 1
        actual = sud.move_character(my_character)
        self.assertTrue(my_character['current_location'] == expected_new_location,
                        "Patched user input typed 'd' for West direction.")