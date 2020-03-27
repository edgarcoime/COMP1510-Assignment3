from unittest import TestCase
from unittest.mock import patch
from lumber_company import harvest_one_tree
from tree_farm import TreeFarm
from tree import Tree
import io  # NEW
import math


class TestHarvestOneTree(TestCase):
    @patch('builtins.input', side_effect=[100])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_harvest_one_tree_100cm_Harvest_Ailanthus(self, mock_stdout, _):
        trees = TreeFarm()
        trees.add(Tree("Maple", 150, 50.23))
        trees.add(Tree("Ailanthus", 10, 104.23))
        trees.add(Tree("Oak", 245, 211))
        actual = str(harvest_one_tree(trees))
        expected = '[Tree("Maple", 150, 50.23), Tree("Oak", 245, 211)]'
        expected_print = "You have harvested the Ailanthus tree that is 10 old.\n"
        self.assertEqual(expected, actual)
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=[50])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_harvest_one_tree_harvest_Maple(self, mock_stdout, _):
        trees = TreeFarm()
        trees.add(Tree("Maple", 150, 50.23))
        trees.add(Tree("Ailanthus", 10, 104.23))
        trees.add(Tree("Oak", 245, 211))
        actual = str(harvest_one_tree(trees))
        expected = '[Tree("Ailanthus", 10, 104.23), Tree("Oak", 245, 211)]'
        expected_print = "You have harvested the Maple tree that is 150 old.\n"
        self.assertEqual(expected, actual)
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=[250])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_harvest_one_trees_harvest_no_tress(self, mock_stdout, _):
        trees = TreeFarm()
        trees.add(Tree("Maple", 150, 50.23))
        trees.add(Tree("Ailanthus", 10, 104.23))
        trees.add(Tree("Oak", 245, 211))
        actual = str(harvest_one_tree(trees))
        expected = '[Tree("Maple", 150, 50.23), Tree("Ailanthus", 10, 104.23), Tree("Oak", 245, 211)]'
        expected_print = ""
        self.assertEqual(expected, actual)
        self.assertEqual(expected_print, mock_stdout.getvalue())
