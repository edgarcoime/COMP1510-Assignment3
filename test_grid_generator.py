"""
test grid_generator function to see if grid is properly displayed with different values for the param.
"""

from unittest import TestCase

import unittest.mock
import io
import sud


class TestGridGenerator(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_grid_generator_just_character_location(self, mock_stdout):
        my_character = {
            'Name': 'jason',
            'HP': [15, 10],
            'current_location': (3, 3)
        }
        grid_events = {
            'bosses': {}
        }

        expected_print = "[C] = Your character named jason\n" \
                         "[D] = Cetus the Dragon || [W] = Fenrir the Great Wolf || [G] = Ajax the Giant\n\n" \
                         "[ ][ ][ ][ ][ ]\n" \
                         "[ ][ ][ ][ ][ ]\n" \
                         "[ ][ ][C][ ][ ]\n" \
                         "[ ][ ][ ][ ][ ]\n" \
                         "[ ][ ][ ][ ][ ]\n\n" \
                         "You have 10HP\n" \
                         "0/3 bosses are still alive!\n" \
                         "You must kill them to be free of this nightmare!\n\n"

        sud.grid_generator(my_character, grid_events)
        self.assertEqual(mock_stdout.getvalue(), expected_print, "Character location only no bosses.")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_grid_generator_one_boss_alive_health_full(self, mock_stdout):
        my_character = {
            'Name': 'jason',
            'HP': [15, 15],
            'current_location': (1, 1)
        }
        grid_events = {
            'bosses': {(1, 3): 'dragon'}
        }

        expected_print = "[C] = Your character named jason\n" \
                         "[D] = Cetus the Dragon || [W] = Fenrir the Great Wolf || [G] = Ajax the Giant\n\n" \
                         "[C][ ][ ][ ][ ]\n" \
                         "[ ][ ][ ][ ][ ]\n" \
                         "[D][ ][ ][ ][ ]\n" \
                         "[ ][ ][ ][ ][ ]\n" \
                         "[ ][ ][ ][ ][ ]\n\n" \
                         "You have 15HP\n" \
                         "1/3 bosses are still alive!\n" \
                         "You must kill them to be free of this nightmare!\n\n"

        sud.grid_generator(my_character, grid_events)
        self.assertEqual(mock_stdout.getvalue(), expected_print, "Character top left and only dragon boss.")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_grid_generator_two_boss_alive_health_low(self, mock_stdout):
        my_character = {
            'Name': 'jason',
            'HP': [15, 1],
            'current_location': (5, 1)
        }
        grid_events = {
            'bosses': {(1, 3): 'dragon',
                       (3, 3): 'wolf'}
        }

        expected_print = "[C] = Your character named jason\n" \
                         "[D] = Cetus the Dragon || [W] = Fenrir the Great Wolf || [G] = Ajax the Giant\n\n" \
                         "[ ][ ][ ][ ][C]\n" \
                         "[ ][ ][ ][ ][ ]\n" \
                         "[D][ ][W][ ][ ]\n" \
                         "[ ][ ][ ][ ][ ]\n" \
                         "[ ][ ][ ][ ][ ]\n\n" \
                         "You have 1HP\n" \
                         "2/3 bosses are still alive!\n" \
                         "You must kill them to be free of this nightmare!\n\n"

        sud.grid_generator(my_character, grid_events)
        self.assertEqual(mock_stdout.getvalue(), expected_print, "Character top right and dragon and wolf boss.")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_grid_generator_all_boss_alive_character_bottom_left(self, mock_stdout):
        my_character = {
            'Name': 'jason',
            'HP': [15, 7],
            'current_location': (1, 5)
        }
        grid_events = {
            'bosses': {(1, 3): 'dragon',
                       (3, 3): 'wolf',
                       (5, 3): 'giant'}
        }

        expected_print = "[C] = Your character named jason\n" \
                         "[D] = Cetus the Dragon || [W] = Fenrir the Great Wolf || [G] = Ajax the Giant\n\n" \
                         "[ ][ ][ ][ ][ ]\n" \
                         "[ ][ ][ ][ ][ ]\n" \
                         "[D][ ][W][ ][G]\n" \
                         "[ ][ ][ ][ ][ ]\n" \
                         "[C][ ][ ][ ][ ]\n\n" \
                         "You have 7HP\n" \
                         "3/3 bosses are still alive!\n" \
                         "You must kill them to be free of this nightmare!\n\n"

        sud.grid_generator(my_character, grid_events)
        self.assertEqual(mock_stdout.getvalue(), expected_print, "Character bottom left and all bosses are alive.")
