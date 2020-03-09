from unittest import TestCase
import sud
import unittest.mock  # NEW
import io  # NEW


class TestMoveSouth(TestCase):
    def test_move_south_from_1_1_move_1_2(self):
        character = {'current_location': (1, 1)}
        expected = (1, 2)
        sud.move_south(character)
        self.assertEqual(expected, character['current_location'])

    def test_move_south_from_3_3_move_3_4(self):
        character = {'current_location': (3, 3)}
        expected = (3, 4)
        sud.move_south(character)
        self.assertEqual(expected, character['current_location'])

    def test_move_south_from_5_4_move_5_5(self):
        character = {'current_location': (5, 4)}
        expected = (5, 5)
        sud.move_south(character)
        self.assertEqual(expected, character['current_location'])

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_move_south_from_x_is_1_and_y_is_5_fail(self, mock_stdout):
        character = {'current_location': (1, 5)}
        sud.move_south(character)
        expected = """The Southern wall of the colosseum towers before you.
You cannot go any more South! Turn back.\n"""
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_move_south_from_x_is_2_and_y_is_5_fail(self, mock_stdout):
        character = {'current_location': (2, 5)}
        sud.move_south(character)
        expected = """The Southern wall of the colosseum towers before you.
You cannot go any more South! Turn back.\n"""
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_move_south_from_x_is_3_and_y_is_5_fail(self, mock_stdout):
        character = {'current_location': (3, 5)}
        sud.move_south(character)
        expected = """The Southern wall of the colosseum towers before you.
You cannot go any more South! Turn back.\n"""
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_move_south_from_x_is_4_and_y_is_5_fail(self, mock_stdout):
        character = {'current_location': (4, 5)}
        sud.move_south(character)
        expected = """The Southern wall of the colosseum towers before you.
You cannot go any more South! Turn back.\n"""
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_move_south_from_x_is_5_and_y_is_5_fail(self, mock_stdout):
        character = {'current_location': (5, 5)}
        sud.move_south(character)
        expected = """The Southern wall of the colosseum towers before you.
You cannot go any more South! Turn back.\n"""
        self.assertEqual(mock_stdout.getvalue(), expected)
