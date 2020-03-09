"""
test attack function that determines how much damage attacker does to defender depending on rolls and sides.
"""
from unittest import TestCase

import unittest.mock
import io
import sud


class TestAttacking(TestCase):

    @unittest.mock.patch('sud.roll_die', side_effect=[6])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_default_values_killing_defender(self, mock_stdout, _):
        attacker = {
            'Name': 'Edgar',
            'HP': [15, 15],
        }
        defender = {
            'Name': 'ENEMY',
            'HP': [5, 5]
        }

        expected_print = "Edgar attacks ENEMY and deals 6 damage.\n" \
                         "Leaving ENEMY with -1/5HP.\n\n"
        expected_HP = [5, -1]
        sud.attack(attacker, defender)
        self.assertEqual(mock_stdout.getvalue(), expected_print, "The attack kills def, leaving -1/5HP.")
        self.assertTrue(defender['HP'] == expected_HP)

    @unittest.mock.patch('sud.roll_die', side_effect=[3])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_default_values_defender_alive(self, mock_stdout, _):
        attacker = {
            'Name': 'Edgar',
            'HP': [15, 15],
        }
        defender = {
            'Name': 'ENEMY',
            'HP': [5, 5]
        }

        expected_print = "Edgar attacks ENEMY and deals 3 damage.\n" \
                         "Leaving ENEMY with 2/5HP.\n\n"
        expected_HP = [5, 2]
        sud.attack(attacker, defender)
        self.assertEqual(mock_stdout.getvalue(), expected_print, "The attack leaves def with 2/5HP.")
        self.assertTrue(defender['HP'] == expected_HP)

    @unittest.mock.patch('sud.roll_die', side_effect=[2, 3])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_times_attack_changed_attack_twice(self, mock_stdout, _):
        char = {
            'Name': 'Edgar',
            'HP': [15, 15],
        }
        monster = {
            'Name': 'ENEMY',
            'HP': [5, 5]
        }

        expected_print = "Edgar attacks with tremendous speed! Allowing it to strike ENEMY 2 times.\n" \
                         "Edgar rolls 2, 3 for a total of 5 damage. Leaving ENEMY with 0/5HP.\n\n"
        expected_HP = [5, 0]
        sud.attack(char, monster, times_attack=2)
        self.assertEqual(mock_stdout.getvalue(), expected_print, "The attacker rolls dmg twice, leaving def with 1HP.")
        self.assertTrue(monster['HP'] == expected_HP)

    @unittest.mock.patch('sud.roll_die', side_effect=[24, 14, 9, 18])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_all_default_values_changed(self, mock_stdout, _):
        char = {
            'Name': 'Edgar',
            'HP': [15, 15],
        }
        monster = {
            'Name': 'ENEMY',
            'HP': [5, 5]
        }

        expected_print = "ENEMY attacks with tremendous speed! Allowing it to strike Edgar 4 times.\n" \
                         "ENEMY rolls 24, 14, 9, 18 for a total of 65 damage. Leaving Edgar with -50/15HP.\n\n"
        expected_HP = [15, -50]
        sud.attack(monster, char, times_attack=4, roll=3, side=8)
        self.assertEqual(mock_stdout.getvalue(), expected_print, "The attacker rolls dmg twice, leaving def with 1HP.")
        self.assertTrue(char['HP'] == expected_HP)
