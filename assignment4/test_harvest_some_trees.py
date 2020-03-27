from unittest import TestCase
from unittest.mock import patch
from lumber_company import harvest_some_trees
from tree_farm import TreeFarm
from tree import Tree
import io  # NEW
import math


class TestHarvestSomeTrees(TestCase):
    @patch('builtins.input', side_effect=[100])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_harvest_some_trees_100cm_circumference_up(self, mock_stdout, _):
        trees = TreeFarm()
        trees.add(Tree("Maple", 150, 50.23))
        trees.add(Tree("Ailanthus", 10, 104.23))
        trees.add(Tree("Oak", 245, 211))
        actual = str(harvest_some_trees(trees))
        expected = '[Tree("Maple", 150, 50.23)]'
        expected_print = """You have harvested the Ailanthus tree that is 10 old.
You have harvested the Oak tree that is 245 old.
We have removed the following trees:
 - Harvested the Maple tree that was 150 years old.
These are the trees in the tree farm:
There is a Maple tree that is 150 years old.\n"""
        self.assertEqual(expected, actual)
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=[50])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_harvest_some_trees_harvest_all_tress(self, mock_stdout, _):
        trees = TreeFarm()
        trees.add(Tree("Maple", 150, 50.23))
        trees.add(Tree("Ailanthus", 10, 104.23))
        trees.add(Tree("Oak", 245, 211))
        actual = str(harvest_some_trees(trees))
        expected = '[]'
        expected_print = """You have harvested the Maple tree that is 150 old.
You have harvested the Ailanthus tree that is 10 old.
You have harvested the Oak tree that is 245 old.
We have removed the following trees:
These are the trees in the tree farm:\n"""
        self.assertEqual(expected, actual)
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=[250])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_harvest_some_trees_harvest_no_tress(self, mock_stdout, _):
        trees = TreeFarm()
        trees.add(Tree("Maple", 150, 50.23))
        trees.add(Tree("Ailanthus", 10, 104.23))
        trees.add(Tree("Oak", 245, 211))
        actual = str(harvest_some_trees(trees))
        expected = '[Tree("Maple", 150, 50.23), Tree("Ailanthus", 10, 104.23), Tree("Oak", 245, 211)]'
        expected_print = """We have removed the following trees:
 - Harvested the Maple tree that was 150 years old.
 - Harvested the Ailanthus tree that was 10 years old.
 - Harvested the Oak tree that was 245 years old.
These are the trees in the tree farm:
There is a Maple tree that is 150 years old.
There is a Ailanthus tree that is 10 years old.
There is a Oak tree that is 245 years old.\n"""
        self.assertEqual(expected, actual)
        self.assertEqual(expected_print, mock_stdout.getvalue())
