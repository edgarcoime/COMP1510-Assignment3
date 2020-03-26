import math
from tree import Tree
from tree_farm import TreeFarm


def add_tree(tree_farm: list) -> list:
    """
    Ask the specific info about a tree: species, age and circumference with the blow conditions. Next, add the new tree
    object into the tree_farm list and return tree_farm. Otherwise, give an exception of ValueError and return the
    original tree_farm list
    precondition: tree_farm must be a list containing object only
    postcondition: Except ValueError at creating an object of tree and print error message if putting wrong format of
    species, age or circumference. Except TypeError at add function and print error message if tree is not an object.
    Finally, return tree_farm is list after adding an tree object.
    :param tree_farm: must be a list containing object only
    :return: Return tree_farm anyway. If no error appears, add one tree object into tree_farm list.
    """
    species = input("What species is the tree? ")
    age = input("What is the tree's age? ")
    circumference = input("What is the tree's circumference? ")
    try:
        tree = Tree(species, int(age), float(circumference))
    except ValueError:
        print("You only can provide non-empty species, positive integer age and non-zero positive float circumference.")
        return tree_farm
    else:
        try:
            tree_farm.add(tree)
        except TypeError:
            print("The tree must be an object.")
            return tree_farm
        else:
            tree_farm.print_trees()
    return tree_farm


def harvest_one_tree(tree_farm: list) -> list:
    """
    Aak the diameter and accord to the value to match the first object matching the requirement. Remove the object and
    return tree_farm list.
    precondition: tree_farm must be a list containing object only
    postcondition: Except ValueError at calculating the circumference and print error message if putting wrong format of
    circumference. Return tree_farm is list after removing the first tree object which is larger or equal to the circumference.
    :param tree_farm: must be a list containing object only
    :return: Return tree_farm anyway. If no error appears, remove one tree object and return tree_farm list.
    """
    diameter = input("What diameter tree would you like? ")
    try:
        circumference = math.pi * float(diameter)
    except ValueError:
        print("The float format only")
        return tree_farm
    else:
        tree_farm.remove_tree(circumference)
        tree_farm.print_trees()
    return tree_farm


def harvest_some_trees(tree_farm: list) -> list:
    """
    Aak the diameter and accord to the value to match the every object which is larger than or equal to the circumference.
    Remove the objects and return tree_farm list.
    precondition: tree_farm must be a list containing object only
    postcondition: Except ValueError at calculating the circumference and print error message if putting wrong format of
    circumference. Return tree_farm is list after removing the every object  which is larger than or equal to the circumference.
    :param tree_farm: must be a list containing object only
    :return: Return tree_farm anyway. If no error appears, remove the objects which is larger than or equal to
    the circumference and return tree_farm list.
    """
    diameter = input("What diameter tree would you like? ")
    try:
        circumference = math.pi * float(diameter)
    except ValueError:
        print("The float format only")
        return tree_farm
    else:
        tree_farm.remove_trees(circumference)
        tree_farm.print_trees()
    return tree_farm


def main():
    tree_farm = TreeFarm()
    while True:
        ask_options = input("""
        1. Add a Tree
        2. Harvest one Tree
        3. Harvest some Trees
        4. Quit
        """)
        if ask_options.strip() == str(1):
            tree_farm = add_tree(tree_farm)
        elif ask_options.strip() == str(2):
            tree_farm = harvest_one_tree(tree_farm)
        elif ask_options.strip() == str(3):
            tree_farm = harvest_some_trees(tree_farm)
        elif ask_options.strip() == str(4):
            break
        else:
            print("Please only type 1, 2, 3 or 4")


if __name__ == '__main__':
    main()
