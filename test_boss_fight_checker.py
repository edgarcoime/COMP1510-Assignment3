from unittest import TestCase
import sud


class TestBossFightChecker(TestCase):
    def test_boss_fight_checker_meet_dragon_at_1_1(self):
        character = {'current_location': (1, 1)}
        grid_events = {
            'bosses': {(1, 1): 'dragon',
                       (5, 1): 'giant',
                       (5, 5): 'wolf'},
            'events': None
        }
        actual = sud.boss_fight_checker(character, grid_events)
        expected = 'dragon'
        self.assertEqual(expected, actual)

    def test_boss_fight_checker_meet_giant_at_5_1(self):
        character = {'current_location': (5, 1)}
        grid_events = {
            'bosses': {(1, 1): 'dragon',
                       (5, 1): 'giant',
                       (5, 5): 'wolf'},
            'events': None
        }
        actual = sud.boss_fight_checker(character, grid_events)
        expected = 'giant'
        self.assertEqual(expected, actual)

    def test_boss_fight_checker_meet_wolf_at_5_5(self):
        character = {'current_location': (5, 5)}
        grid_events = {
            'bosses': {(1, 1): 'dragon',
                       (5, 1): 'giant',
                       (5, 5): 'wolf'},
            'events': None
        }
        actual = sud.boss_fight_checker(character, grid_events)
        expected = 'wolf'
        self.assertEqual(expected, actual)

    def test_boss_fight_checker_do_not_meet_boss_false_first_case(self):
        character = {'current_location': (2, 3)}
        grid_events = {
            'bosses': {(1, 1): 'dragon',
                       (5, 1): 'giant',
                       (5, 5): 'wolf'},
            'events': None
        }
        actual = sud.boss_fight_checker(character, grid_events)
        self.assertFalse(actual)

    def test_boss_fight_checker_do_not_meet_boss_false_second_case(self):
        character = {'current_location': (5, 4)}
        grid_events = {
            'bosses': {(1, 1): 'dragon',
                       (5, 1): 'giant',
                       (5, 5): 'wolf'},
            'events': None
        }
        actual = sud.boss_fight_checker(character, grid_events)
        self.assertFalse(actual)
