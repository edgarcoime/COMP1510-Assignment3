from unittest import TestCase
from unittest.mock import patch
from assignment4.lumber_company import harvest_some_trees
from assignment4.tree_farm import TreeFarm
from assignment4.tree import Tree
import io  # NEW


class TestHarvestSomeTrees(TestCase):
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

    @patch('builtins.input', side_effect=[100])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_harvest_some_trees_100cm_circumference_up(self, mock_stdout, _):
        expected_print = """We have removed the following trees:
 - Harvested the Ailanthus tree that was 10 years old.
 - Harvested the Oak tree that was 245 years old.
These are the trees in the tree farm:
There is a Maple tree that is 150 years old.\n"""
        harvest_some_trees(self.test_tree_farm_3_trees)
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=[10])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_harvest_some_trees_harvest_all_trees(self, mock_stdout, _):
        expected_print = """We have removed the following trees:
 - Harvested the Maple tree that was 150 years old.
 - Harvested the Ailanthus tree that was 10 years old.
 - Harvested the Oak tree that was 245 years old.
These are the trees in the tree farm:
"""
        harvest_some_trees(self.test_tree_farm_3_trees)
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=[250])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_harvest_some_trees_harvest_no_trees(self, mock_stdout, _):
        expected_print = """We have removed the following trees:
These are the trees in the tree farm:
There is a Maple tree that is 150 years old.
There is a Ailanthus tree that is 10 years old.
There is a Oak tree that is 245 years old.\n"""
        harvest_some_trees(self.test_tree_farm_3_trees)
        self.assertEqual(expected_print, mock_stdout.getvalue())
