import math
from tree import Tree
from treefram import TreeFarm


def platform():
    tree_farm = TreeFarm()
    while True:
        ask_options = input("""
        1. Add a Tree
        2. Harvest one Tree
        3. Harvest some Trees
        4. Quit
        """)
        if ask_options == str(1):
            tree_farm = add_tree(tree_farm)
        elif ask_options == str(2):
            tree_farm = harvest_one_tree(tree_farm)
        elif ask_options == str(3):
            tree_farm = harvest_some_trees(tree_farm)
        elif ask_options == str(4):
            break
        else:
            print("please type 1,2,3 or 4")


def add_tree(tree_farm):
    species = input("What is the species?")
    age = input("What is the tree's age?")
    circumference = input("What is the tree's circumference?")
    tree_farm.add(Tree(species, int(age), float(circumference)))
    tree_farm.print_tree()
    return tree_farm


def harvest_one_tree(tree_farm):
    diameter = input("What is the tree's diameter?")
    circumference = math.pi * float(diameter)
    tree_farm.remove_tree(circumference)
    tree_farm.print_tree()
    return tree_farm


def harvest_some_trees(tree_farm):
    diameter = input("What is the tree's diameter?")
    circumference = math.pi * float(diameter)
    tree_farm.remove_trees(circumference)
    tree_farm.print_tree()
    return tree_farm


def main():
    platform()


if __name__ == '__main__':
    main()
