"""
test combat round function that determines whether another battle exchange should be displayed or a death screen.
"""
from unittest import TestCase

import unittest.mock
import io
import sud


class TestCombatRound(TestCase):

    @unittest.mock.patch('sud.roll_die', side_effect=[6])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_kill_enemy(self, mock_stdout, _):
        char = {
            'Name': 'Edgar',
            'HP': [15, 15],
        }
        monster = {
            'Name': 'ENEMY',
            'HP': [5, 5]
        }

        expected_print = "Edgar draws his weapon and lunges at the beast.\n" \
                         "Edgar attacks ENEMY and deals 6 damage.\n" \
                         "Leaving ENEMY with -1/5HP.\n\n" \
                         "You have successfully killed the monster ENEMY!\n\n"
        char_expected_HP = [15, 15]
        monster_expected_HP = [5, -1]
        sud.combat_round(char, monster)
        self.assertEqual(mock_stdout.getvalue(), expected_print, "The Character kills monster.")
        self.assertTrue(char['HP'] == char_expected_HP)
        self.assertTrue(monster['HP'] == monster_expected_HP)


    @unittest.mock.patch('sud.roll_die', side_effect=[4, 6])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_both_alive(self, mock_stdout, _):
        char = {
            'Name': 'Edgar',
            'HP': [15, 15],
        }
        monster = {
            'Name': 'ENEMY',
            'HP': [5, 5]
        }

        expected_print = "Edgar draws his weapon and lunges at the beast.\n" \
                         "Edgar attacks ENEMY and deals 4 damage.\n" \
                         "Leaving ENEMY with 1/5HP.\n\n" \
                         "ENEMY staggers and recovers its composure. It glares at you and Retaliates!\n" \
                         "ENEMY attacks Edgar and deals 6 damage.\n" \
                         "Leaving Edgar with 9/15HP.\n\n"
        char_expected_HP = [15, 9]
        monster_expected_HP = [5, 1]
        sud.combat_round(char, monster)
        self.assertEqual(mock_stdout.getvalue(), expected_print, "The Character kills monster.")
        self.assertTrue(char['HP'] == char_expected_HP)
        self.assertTrue(monster['HP'] == monster_expected_HP)


    @unittest.mock.patch('sud.roll_die', side_effect=[4, 6])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_character_is_killed(self, mock_stdout, _):
        char = {
            'Name': 'Edgar',
            'HP': [15, 4],
        }
        monster = {
            'Name': 'ENEMY',
            'HP': [5, 5]
        }

        expected_print = "Edgar draws his weapon and lunges at the beast.\n" \
                         "Edgar attacks ENEMY and deals 4 damage.\n" \
                         "Leaving ENEMY with 1/5HP.\n\n" \
                         "ENEMY staggers and recovers its composure. It glares at you and Retaliates!\n" \
                         "ENEMY attacks Edgar and deals 6 damage.\n" \
                         "Leaving Edgar with -2/15HP.\n\n" \
                         "You are dealt a fatal wound and everything turns black. " \
                         "All you hear are the monsters gathering \n" \
                         "around your body and the sound of your flesh being eaten.\n"
        char_expected_HP = [15, -2]
        monster_expected_HP = [5, 1]
        sud.combat_round(char, monster)
        self.assertEqual(mock_stdout.getvalue(), expected_print, "The monster kills the user character")
        self.assertTrue(char['HP'] == char_expected_HP)
        self.assertTrue(monster['HP'] == monster_expected_HP)