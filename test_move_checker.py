from unittest import TestCase
import sud
from unittest.mock import patch
import io  # NEW


class TestMoveChecker(TestCase):
    @patch('sud.roll_die', side_effect=[1])
    def test_movement_checker_roll_1_meet_monster_true(self, _):
        character = {'HP': [15, 15]}
        actual = sud.movement_checker(character)
        self.assertTrue(actual)

    @patch('sud.roll_die', side_effect=[2])
    def test_movement_checker_roll_2_meet_monster_false(self, _):
        character = {'HP': [15, 15]}
        actual = sud.movement_checker(character)
        self.assertFalse(actual)

    @patch('sud.roll_die', side_effect=[4])
    def test_movement_checker_roll_4_meet_monster_false(self, _):
        character = {'HP': [15, 15]}
        actual = sud.movement_checker(character)
        self.assertFalse(actual)

    @patch('sud.roll_die', side_effect=[2])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_movement_checker_roll_2_meet_monster_false_full_hp(self, mock_stdout, _):
        character = {'HP': [15, 15]}
        sud.movement_checker(character)
        expected = """You were too fast for the onslaught of monsters. They couldn't catch you.
You are in pretty good condition and don't need bandaging. You have 15/15HP\n\n"""
        self.assertEqual(expected, mock_stdout.getvalue())


    @patch('sud.roll_die', side_effect=[2])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_movement_checker_roll_2_meet_monster_false_hp_15_13_to_15_15(self, mock_stdout, _):
        character = {'HP': [15, 13]}
        sud.movement_checker(character)
        expected = """The monsters couldn't catch up to you. This gives you the opportunity to bandage your wounds.
You heal 2 points. You now have 15/15HP\n\n"""
        self.assertEqual(expected, mock_stdout.getvalue())

