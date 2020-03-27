from unittest import TestCase
from unittest.mock import patch
from assignment4.lumber_company import harvest_one_tree
from assignment4.tree_farm import TreeFarm
from assignment4.tree import Tree
import io  # NEW


class TestHarvestOneTree(TestCase):

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
    def test_harvest_one_tree_100cm_Harvest_Ailanthus(self, mock_stdout, _):
        expected_print = "We have harvested the Ailanthus tree that was 10 years old.\n\n" \
                         "These are the trees in the tree farm:\n" \
                         "There is a Maple tree that is 150 years old.\n" \
                         "There is a Oak tree that is 245 years old.\n"
        harvest_one_tree(self.test_tree_farm_3_trees)
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=[50])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_harvest_one_tree_harvest_Maple(self, mock_stdout, _):
        expected_print = "We have harvested the Maple tree that was 150 years old.\n\n" \
                         "These are the trees in the tree farm:\n" \
                         "There is a Ailanthus tree that is 10 years old.\n" \
                         "There is a Oak tree that is 245 years old.\n"
        harvest_one_tree(self.test_tree_farm_3_trees)
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=[1000])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_harvest_one_trees_harvest_no_tress(self, mock_stdout, _):
        expected_print = "We found no trees with that given circumference.\n"
        harvest_one_tree(self.test_tree_farm_3_trees)
        self.assertEqual(expected_print, mock_stdout.getvalue())
