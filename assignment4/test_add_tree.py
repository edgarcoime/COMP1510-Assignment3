from unittest import TestCase
from unittest.mock import patch
from assignment4.lumber_company import add_tree
from assignment4.tree_farm import TreeFarm
from assignment4.tree import Tree
import io  # NEW


class TestAddTree(TestCase):

    def setUp(self) -> None:
        self.test_tree_1 = Tree("Maple", 150, 50.23)
        self.test_tree_2 = Tree("Ailanthus", 10, 104.23)
        self.test_tree_3 = Tree("Oak", 245, 211)

        # empty tree farm
        self.test_tree_farm_empty = TreeFarm()

        # single tree Tree farm
        self.test_tree_farm_1_tree = TreeFarm()
        self.test_tree_farm_1_tree.add(self.test_tree_1)

        # Tree farm with 2 trees
        self.test_tree_farm_2_trees = TreeFarm()
        self.test_tree_farm_2_trees.add(self.test_tree_1)
        self.test_tree_farm_2_trees.add(self.test_tree_2)

        # Tree farm with 3 trees
        self.test_tree_farm_3_trees = TreeFarm()
        self.test_tree_farm_3_trees.add(self.test_tree_1)
        self.test_tree_farm_3_trees.add(self.test_tree_2)
        self.test_tree_farm_3_trees.add(self.test_tree_3)


    @patch('builtins.input', side_effect=["Ailanthus", 10, 104.23])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_tree_valid_input_add_one_tree(self, mock_stdout, _):

        expected_print = "These are the trees in the tree farm:\n" \
                         "There is a Ailanthus tree that is 10 years old.\n"
        add_tree(self.test_tree_farm_empty)
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=[" ", 10, 104.23])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_tree_invalid_input_add_empty_species(self, mock_stdout, _):
        add_tree(self.test_tree_farm_empty)
        self.assertEqual(
            "You only can provide non-empty species, positive integer age and non-zero positive float circumference.\n",
            mock_stdout.getvalue())

    @patch('builtins.input', side_effect=["Ailanthus", -1, 104.23])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_tree_invalid_input_add_negative_age(self, mock_stdout, _):
        add_tree(self.test_tree_farm_empty)
        self.assertEqual(
            "You only can provide non-empty species, positive integer age and non-zero positive float circumference.\n",
            mock_stdout.getvalue())

    @patch('builtins.input', side_effect=["Ailanthus", 10, -10.47])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_tree_invalid_input_add_negative_circumference(self, mock_stdout, _):
        add_tree(self.test_tree_farm_empty)
        self.assertEqual(
            "You only can provide non-empty species, positive integer age and non-zero positive float circumference.\n",
            mock_stdout.getvalue())

    @patch('builtins.input', side_effect=["Ailanthus", 10, "not a number"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_tree_invalid_input_add_wrong_input_format(self, mock_stdout, _):
        add_tree(self.test_tree_farm_empty)
        self.assertEqual(
            "You only can provide non-empty species, positive integer age and non-zero positive float circumference.\n",
            mock_stdout.getvalue())