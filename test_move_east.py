from unittest import TestCase
import sud
import unittest.mock  # NEW
import io  # NEW


class TestMoveEast(TestCase):
    def test_move_east_from_1_1_move_2_1(self):
        character = {'current_location': (1, 1)}
        expected = (2, 1)
        sud.move_east(character)
        self.assertEqual(expected, character['current_location'])

    def test_move_east_from_3_3_move_4_3(self):
        character = {'current_location': (3, 3)}
        expected = (4, 3)
        sud.move_east(character)
        self.assertEqual(expected, character['current_location'])

    def test_move_east_from_4_5_move_5_5(self):
        character = {'current_location': (4, 5)}
        expected = (5, 5)
        sud.move_east(character)
        self.assertEqual(expected, character['current_location'])

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_move_east_from_x_is_1_and_y_is_1_fail(self, mock_stdout):
        character = {'current_location': (5, 1)}
        sud.move_east(character)
        expected = """The Eastern wall of the colosseum towers before you.
You cannot go any more East! Turn back.\n"""
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_move_east_from_x_is_1_and_y_is_2_fail(self, mock_stdout):
        character = {'current_location': (5, 2)}
        sud.move_east(character)
        expected = """The Eastern wall of the colosseum towers before you.
You cannot go any more East! Turn back.\n"""
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_move_east_from_x_is_1_and_y_is_3_fail(self, mock_stdout):
        character = {'current_location': (5, 3)}
        sud.move_east(character)
        expected = """The Eastern wall of the colosseum towers before you.
You cannot go any more East! Turn back.\n"""
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_move_east_from_x_is_1_and_y_is_4_fail(self, mock_stdout):
        character = {'current_location': (5, 4)}
        sud.move_east(character)
        expected = """The Eastern wall of the colosseum towers before you.
You cannot go any more East! Turn back.\n"""
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_move_east_from_x_is_1_and_y_is_5_fail(self, mock_stdout):
        character = {'current_location': (5, 5)}
        sud.move_east(character)
        expected = """The Eastern wall of the colosseum towers before you.
You cannot go any more East! Turn back.\n"""
        self.assertEqual(mock_stdout.getvalue(), expected)
