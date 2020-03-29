import doctest
from assignment4.tree import Tree
from assignment4.tree_farm import TreeFarm


def add_tree(tree_farm: object) -> None:
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
    circumference = input("What is the tree's circumference?\n")
    try:
        tree = Tree(species, int(age), float(circumference))
        tree_farm.add(tree)
    except (ValueError, TypeError):
        print("You only can provide non-empty species, positive integer age and non-zero positive float circumference.")
    else:
        tree_farm.print_trees()


def harvest_one_tree(tree_farm: object) -> None:
    """
    Aak the diameter and accord to the value to match the first object matching the requirement. Remove the object and
    return tree_farm list.
    precondition: tree_farm must be a list containing object only
    postcondition: Except ValueError at calculating the circumference and print error message if putting wrong format of
    circumference. Return tree_farm is list after removing the first tree object which is larger or equal to the
    circumference.
    :param tree_farm: must be a list containing object only
    :return: Return tree_farm anyway. If no error appears, remove one tree object and return tree_farm list.
    """
    circumference = input("What Circumference tree would you like?\n")
    try:
        removed_tree = tree_farm.remove_tree(float(circumference))
    except ValueError:
        print("Input must be of type float only!")
    else:
        if removed_tree == None:
            print("We found no trees with that given circumference.")
        else:
            print(
                f"We have harvested the {removed_tree.get_species()} tree that was {removed_tree.get_age()} years old.\n")
            tree_farm.print_trees()


def harvest_some_trees(tree_farm: object) -> None:
    """
    Ask the diameter and accord to the value to match the every object which is larger than or equal to the
    circumference. Remove the objects and return tree_farm list.

    precondition: tree_farm must be a list containing object only
    postcondition: Except ValueError at calculating the circumference and print error message if putting wrong format of
    circumference. Return tree_farm is list after removing the every object  which is larger than or equal to the
    circumference.
    :param tree_farm: must be a list containing object only
    :return: Return tree_farm anyway. If no error appears, remove the objects which is larger than or equal to
    the circumference and return tree_farm list.
    """
    circumference = input("What Circumference tree would you like?\n")
    try:
        removed_trees = tree_farm.remove_trees(float(circumference))
    except ValueError:
        print("Input must be of type float only!")
    else:
        print("We have removed the following trees:")
        for tree in removed_trees:
            print(f" - Harvested the {tree.get_species()} tree that was {tree.get_age()} years old.")
        tree_farm.print_trees()


def main():
    """
    Test the module
    """
    tree_farm = TreeFarm()
    tree_farm.add(Tree("Maple", 150, 50.23))
    tree_farm.add(Tree("Ailanthus", 10, 104.23))
    tree_farm.add(Tree("Oak", 150, 211))
    while True:
        ask_options = input("""
        1. Add a Tree
        2. Harvest one Tree
        3. Harvest some Trees
        4. Quit
        """)
        if ask_options.strip() == str(1):
            add_tree(tree_farm)
        elif ask_options.strip() == str(2):
            harvest_one_tree(tree_farm)
        elif ask_options.strip() == str(3):
            harvest_some_trees(tree_farm)
        elif ask_options.strip() == str(4):
            break
        else:
            print("Please only type 1, 2, 3 or 4")
    doctest.testmod()


if __name__ == '__main__':
    main()
