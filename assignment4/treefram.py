from tree import Tree
from copy import deepcopy


class TreeFarm:
    def __init__(self):
        self.tree_farm = []

    def __str__(self):
        return f"{self.tree_farm}"

    def __repr__(self):
        return f"{self.tree_farm}"

    def get_tree_farm(self):
        return self.tree_farm

    def add(self, tree: object) -> list:
        self.tree_farm.append(tree)
        return self.tree_farm

    def print_tree(self):
        for one_tree in self.tree_farm:
            print(f"{self.tree_farm.index(one_tree) +1 }. The specie is {one_tree.get_species()}, its age is {one_tree.get_age()}")

    def remove_tree(self, trunk_circumference: float) -> list:
        for one_tree in self.tree_farm.copy():
            if one_tree.get_trunk_circumference() >= trunk_circumference:
                self.tree_farm.remove(one_tree)
                return self.tree_farm
        return None

    def remove_trees(self, trunk_circumference: float) -> list:
        for one_tree in self.tree_farm.copy():
            if one_tree.get_trunk_circumference() >= trunk_circumference:
                self.tree_farm.remove(one_tree)
        return self.tree_farm


def main():
    tree1 = Tree("A", 1, 20)
    tree2 = Tree("B", 2, 40)
    tree3 = Tree("C", 3, 10)
    tree_farm1 = TreeFarm()
    tree_farm1.add(tree1)
    tree_farm1.add(tree2)
    tree_farm1.add(tree3)
    tree_farm1.print_tree()
    tree_farm1.remove_trees(10)
    print(tree_farm1)
    tree_farm1.remove_tree(100)
    print(tree_farm1)


if __name__ == '__main__':
    main()
