from unittest import TestCase
import sud
import unittest.mock  # NEW
import io  # NEW


class TestMoveWest(TestCase):
    def test_move_west_from_2_1_move_1_1(self):
        character = {'current_location': (2, 1)}
        expected = (1, 1)
        sud.move_west(character)
        self.assertEqual(expected, character['current_location'])

    def test_move_west_from_3_3_move_2_3(self):
        character = {'current_location': (3, 3)}
        expected = (2, 3)
        sud.move_west(character)
        self.assertEqual(expected, character['current_location'])

    def test_move_west_from_5_5_move_4_5(self):
        character = {'current_location': (5, 5)}
        expected = (4, 5)
        sud.move_west(character)
        self.assertEqual(expected, character['current_location'])

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_move_west_from_x_is_1_and_y_is_1_fail(self, mock_stdout):
        character = {'current_location': (1, 1)}
        sud.move_west(character)
        expected = """The Western wall of the colosseum towers before you.
You cannot go any more West! Turn back.\n"""
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_move_west_from_x_is_1_and_y_is_2_fail(self, mock_stdout):
        character = {'current_location': (1, 2)}
        sud.move_west(character)
        expected = """The Western wall of the colosseum towers before you.
You cannot go any more West! Turn back.\n"""
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_move_west_from_x_is_1_and_y_is_3_fail(self, mock_stdout):
        character = {'current_location': (1, 3)}
        sud.move_west(character)
        expected = """The Western wall of the colosseum towers before you.
You cannot go any more West! Turn back.\n"""
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_move_west_from_x_is_1_and_y_is_4_fail(self, mock_stdout):
        character = {'current_location': (1, 4)}
        sud.move_west(character)
        expected = """The Western wall of the colosseum towers before you.
You cannot go any more West! Turn back.\n"""
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_move_west_from_x_is_1_and_y_is_5_fail(self, mock_stdout):
        character = {'current_location': (1, 5)}
        sud.move_west(character)
        expected = """The Western wall of the colosseum towers before you.
You cannot go any more West! Turn back.\n"""
        self.assertEqual(mock_stdout.getvalue(), expected)
