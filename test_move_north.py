from unittest import TestCase
import sud
import unittest.mock  # NEW
import io  # NEW


class TestMoveNorth(TestCase):
    def test_move_north_from_1_2_move_1_1(self):
        character = {'current_location': (1, 2)}
        expected = (1, 1)
        sud.move_north(character)
        self.assertEqual(expected, character['current_location'])

    def test_move_north_from_3_3_move_3_2(self):
        character = {'current_location': (3, 3)}
        expected = (3, 2)
        sud.move_north(character)
        self.assertEqual(expected, character['current_location'])

    def test_move_north_from_5_5_move_5_4(self):
        character = {'current_location': (5, 5)}
        expected = (5, 4)
        sud.move_north(character)
        self.assertEqual(expected, character['current_location'])

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_move_north_from_x_is_1_and_y_is_1_fail(self, mock_stdout):
        character = {'current_location': (1, 1)}
        sud.move_north(character)
        expected = """The Northern wall of the colosseum towers before you.
You cannot go any more North! Turn back.\n"""
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_move_north_from_x_is_2_and_y_is_1_fail(self, mock_stdout):
        character = {'current_location': (2, 1)}
        sud.move_north(character)
        expected = """The Northern wall of the colosseum towers before you.
You cannot go any more North! Turn back.\n"""
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_move_north_from_x_is_3_and_y_is_1_fail(self, mock_stdout):
        character = {'current_location': (3, 1)}
        sud.move_north(character)
        expected = """The Northern wall of the colosseum towers before you.
You cannot go any more North! Turn back.\n"""
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_move_north_from_x_is_4_and_y_is_1_fail(self, mock_stdout):
        character = {'current_location': (4, 1)}
        sud.move_north(character)
        expected = """The Northern wall of the colosseum towers before you.
You cannot go any more North! Turn back.\n"""
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_move_north_from_x_is_5_and_y_is_1_fail(self, mock_stdout):
        character = {'current_location': (5, 1)}
        sud.move_north(character)
        expected = """The Northern wall of the colosseum towers before you.
You cannot go any more North! Turn back.\n"""
        self.assertEqual(mock_stdout.getvalue(), expected)
