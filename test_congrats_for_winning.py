"""
Test the printing message after defeating bosses
"""
from unittest import TestCase
import sud
import unittest.mock  # NEW
import io  # NEW

class TestCongratsForWinning(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_congrats_for_winning_defeat_dragon_remove_from_dictionary(self, mock_stdout):
        grid_events = {
            'bosses': {(5, 1): 'giant',
                       (5, 5): 'wolf'},
            'events': None
        }
        real_boss = {'Name': 'Cetus the Dragon'}
        expected = """Congratulations! You have beaten Cetus the Dragon
You can now proceed to the other bosses in the arena.
"""
        sud.congrats_for_winning(real_boss, grid_events)
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_congrats_for_winning_defeat_giant_remove_from_dictionary(self, mock_stdout):
        grid_events = {
            'bosses': {(1, 1): 'dragon',
                       (5, 5): 'wolf'},
            'events': None
        }
        real_boss = {'Name': 'Ajax the Giant'}
        expected = """Congratulations! You have beaten Ajax the Giant
You can now proceed to the other bosses in the arena.
"""
        sud.congrats_for_winning(real_boss, grid_events)
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_congrats_for_winning_defeat_wolf_remove_from_dictionary(self, mock_stdout):
        grid_events = {
            'bosses': {(1, 1): 'dragon',
                       (5, 1): 'giant'},
            'events': None
        }
        real_boss = {'Name': 'Fenrir the Great Wolf'}
        expected = """Congratulations! You have beaten Fenrir the Great Wolf
You can now proceed to the other bosses in the arena.
"""
        sud.congrats_for_winning(real_boss, grid_events)
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_congrats_for_winning_defeat_all_three_bosses_remove_from_dictionary(self, mock_stdout):
        grid_events = {
            'bosses': {},
            'events': None
        }
        real_boss = {'Name': 'wolf'}
        expected = """As you stand before the lifeless carcass of wolf the final champion.
You take a deep breath as you are overcome with the elation of escaping this nightmarish arena.
You breath in the last breath of air that you will take in this God forsaken place and look forward
to your new reborn life.
Thank you so much to play our game. Tha game producers are Edgar and Tommy
"""
        sud.congrats_for_winning(real_boss, grid_events)
        self.assertEqual(expected, mock_stdout.getvalue())

