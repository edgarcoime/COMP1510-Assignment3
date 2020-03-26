import math
from tree import Tree
from tree_farm import TreeFarm


def add_tree(tree_farm: list) -> list:
    species = input("What species is the tree? ")
    age = input("What is the tree's age? ")
    circumference = input("What is the tree's circumference? ")
    try:
        tree = Tree(species, int(age), float(circumference))
    except ValueError:
        print("You only can provide non-empty species, positive integer age and non-zero positive float circumference.")
        return tree_farm
    else:
        tree_farm.add(tree)
        tree_farm.print_trees()
    return tree_farm


def harvest_one_tree(tree_farm: list) -> list:
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
