"""
test retreat function that determines if character is backstabbed when retreating and how much damage is inflicted.
"""

from unittest import TestCase

import unittest.mock
import io
import sud


class TestRetreat(TestCase):

    @unittest.mock.patch('sud.roll_die', side_effect=[6])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_retreat_backstab_fails(self, mock_stdout, _):
        char = {
            'Name': 'Edgar',
            'HP': [15, 15],
        }

        expected_print = "You have a 10% chance of being backstabbed.\n" \
                         "You successfully escape!\n\n"
        expected_HP = [15, 15]
        sud.retreat(char)
        self.assertEqual(mock_stdout.getvalue(), expected_print, "No backstab is dealt to character.")
        self.assertTrue(char['HP'] == expected_HP)

    @unittest.mock.patch('sud.roll_die', side_effect=[1, 4])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_retreat_backstab_inflicted(self, mock_stdout, _):
        char = {
            'Name': 'Edgar',
            'HP': [15, 15],
        }

        expected_print = "You have a 10% chance of being backstabbed.\n" \
                         "While retreating you are attacked from behind!\n" \
                         "You are hit with 4 damage, leaving you with 11/15HP.\n\n"
        expected_HP = [15, 11]
        sud.retreat(char)
        self.assertEqual(mock_stdout.getvalue(), expected_print, "Backstab is dealt to user and damage is inflicted.")
        self.assertTrue(char['HP'] == expected_HP)
