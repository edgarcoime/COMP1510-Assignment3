"""
Test the the new copy dictionary from grid_events after removing a key under 'bosses' sub-dictionary
"""
from unittest import TestCase
import sud


class TestUpdateBoss(TestCase):
    def test_update_boss_delete_dragon(self):
        grid_events = {
            'bosses': {(1, 1): 'dragon',
                       (5, 1): 'giant',
                       (5, 5): 'wolf'},
            'events': None
        }
        boss_name = 'dragon'
        expected = {'bosses': {(5, 1): 'giant', (5, 5): 'wolf'}, 'events': None}
        actual = sud.update_boss(boss_name, grid_events)
        self.assertEqual(expected, actual)

    def test_update_boss_delete_giant(self):
        grid_events = {
            'bosses': {(1, 1): 'dragon',
                       (5, 1): 'giant',
                       (5, 5): 'wolf'},
            'events': None
        }
        boss_name = 'giant'
        expected = {'bosses': {(1, 1): 'dragon', (5, 5): 'wolf'}, 'events': None}
        actual = sud.update_boss(boss_name, grid_events)
        self.assertEqual(expected, actual)

    def test_update_boss_delete_wolf(self):
        grid_events = {
            'bosses': {(1, 1): 'dragon',
                       (5, 1): 'giant',
                       (5, 5): 'wolf'},
            'events': None
        }
        boss_name = 'wolf'
        expected = {'bosses': {(1, 1): 'dragon', (5, 1): 'giant'}, 'events': None}
        actual = sud.update_boss(boss_name, grid_events)
        self.assertEqual(expected, actual)
