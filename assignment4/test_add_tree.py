from unittest import TestCase
from unittest.mock import patch
from lumber_company import add_tree
from tree_farm import TreeFarm
import io  # NEW


class TestAddTree(TestCase):

    @patch('builtins.input', side_effect=["Ailanthus", 10, 104.23])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_tree_valid_input_add_one_tree(self, mock_stdout, _):
        test_farm = TreeFarm()
        actual = str(add_tree(test_farm))
        expected = '[Tree("Ailanthus", 10, 104.23)]'
        self.assertEqual(expected, actual)
        self.assertEqual("There is a Ailanthus tree that is 10 years old.\n", mock_stdout.getvalue())


    @patch('builtins.input', side_effect=[" ", 10, 104.23])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_tree_invalid_input_add_empty_species(self, mock_stdout, _):
        test_farm = TreeFarm()
        actual = str(add_tree(test_farm))
        expected = '[]'
        self.assertEqual(expected, actual)
        self.assertEqual(
            "You only can provide non-empty species, positive integer age and non-zero positive float circumference.\n",
            mock_stdout.getvalue())

    @patch('builtins.input', side_effect=["Ailanthus", -1, 104.23])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_tree_invalid_input_add_negative_age(self, mock_stdout, _):
        test_farm = TreeFarm()
        actual = str(add_tree(test_farm))
        expected = '[]'
        self.assertEqual(expected, actual)
        self.assertEqual(
            "You only can provide non-empty species, positive integer age and non-zero positive float circumference.\n",
            mock_stdout.getvalue())

    @patch('builtins.input', side_effect=["Ailanthus", 10, -10.47])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_tree_invalid_input_add_negative_circumference(self, mock_stdout, _):
        test_farm = TreeFarm()
        actual = str(add_tree(test_farm))
        expected = '[]'
        self.assertEqual(expected, actual)
        self.assertEqual(
            "You only can provide non-empty species, positive integer age and non-zero positive float circumference.\n",
            mock_stdout.getvalue())

    @patch('builtins.input', side_effect=["Ailanthus", 10, "not a number"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_tree_invalid_input_add_wrong_input_format(self, mock_stdout, _):
        test_farm = TreeFarm()
        actual = str(add_tree(test_farm))
        expected = str([])
        self.assertEqual(expected, actual)
        self.assertEqual(
            "You only can provide non-empty species, positive integer age and non-zero positive float circumference.\n",
            mock_stdout.getvalue())

    @patch('builtins.input', side_effect=["Ailanthus", 10, 10.242])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_tree_invalid_input_not_an_object(self, mock_stdout, _):
        self.assertEqual('not an object', add_tree("not an object"))
        self.assertEqual("", mock_stdout.getvalue())