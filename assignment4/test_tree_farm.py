"""
Testing the attributes and methods of the TreeFarm class in test_tree
"""

from unittest import TestCase

from assignment4.tree_farm import TreeFarm
from assignment4.tree import Tree
import io
import unittest.mock


class TestTreeFarm(TestCase):

    def setUp(self) -> None:
        # Instantiating Tree objects to add to TreeFarm
        self.test_tree1 = Tree("Oak", 123, 432)
        self.test_tree2 = Tree("Maple", 234, 241)

        # empty tree farm
        self.test_tree_farm_empty = TreeFarm()

        # single tree Tree farm
        self.test_tree_farm_1_tree = TreeFarm()
        self.test_tree_farm_1_tree.add(self.test_tree1)

        # Tree farm with 2 trees
        self.test_tree_farm_2_trees = TreeFarm()
        self.test_tree_farm_2_trees.add(self.test_tree1)
        self.test_tree_farm_2_trees.add(self.test_tree2)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_str__(self, mock_stdout):
        expected_print = "[]\n"
        print(self.test_tree_farm_empty)
        self.assertEqual(mock_stdout.getvalue(), expected_print, "Testing standard print output when called inside "
                                                                 "print statement.")

    def test_repr__(self):
        actual = self.test_tree_farm_empty.__repr__()
        expected = 'TreeFarm():\n' \
                   '[]'
        self.assertEqual(actual, expected)

    def test_get_tree_farm(self):
        actual = self.test_tree_farm_empty.get_tree_farm()
        expected = []
        self.assertEqual(actual, expected, "Testing accessing __tree_farm attribute when the list is empty.")

    def test_get_tree_farm_one_tree(self):
        actual = self.test_tree_farm_1_tree.get_tree_farm()
        expected = [self.test_tree1]
        self.assertEqual(actual, expected, "Testing accessing __tree_farm attribute when the list has 1 Tree object.")

    def test_add_not_an_object(self):
        with self.assertRaises(TypeError):
            argument = "I am a tree"
            TreeFarm.add(argument)

    def test_add(self):
        actual = self.test_tree_farm_2_trees.get_tree_farm()
        expected = [self.test_tree1, self.test_tree2]

        self.assertEqual(actual, expected, "Testing adding Tree's")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_trees(self, mock_stdout):
        self.test_tree_farm_2_trees.print_trees()
        expected_print = "There is a Oak tree that is 123 years old.\n" \
                         "There is a Maple tree that is 234 years old.\n"
        self.assertEqual(mock_stdout.getvalue(), expected_print)

    def test_remove_tree(self):
        actual_return = self.test_tree_farm_2_trees.remove_tree(10)
        expected_return = self.test_tree1

        actual_remaining_trees = self.test_tree_farm_2_trees.get_tree_farm()
        expected_remaining_trees = [self.test_tree2]
        self.assertEqual(actual_return, expected_return, "Test removing 1 tree from the list and returning the removed "
                                                         "Tree.")
        self.assertEqual(actual_remaining_trees, expected_remaining_trees, "Test if the removed Tree was removed"
                                                                           "from the TreeFarm list.")

    def test_remove_trees(self):
        actual_return = self.test_tree_farm_2_trees.remove_trees(10)
        expected_return = [self.test_tree1, self.test_tree2]

        actual_remaining_trees = self.test_tree_farm_2_trees.get_tree_farm()
        expected_remaining_trees = []
        self.assertEqual(actual_return, expected_return, "Test removing 2 trees from the list and returning the "
                                                         "list of removed trees.")
        self.assertEqual(actual_remaining_trees, expected_remaining_trees, "Test if the all the removed Trees were "
                                                                           "removed from the Object's tree_farm list.")
