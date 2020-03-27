from assignment4.tree import Tree


class TreeFarm:

    def __init__(self):

        self.__tree_farm = []

    def __str__(self):
        return f"{self.__tree_farm}"

    def __repr__(self):
        return f"TreeFarm():\n" \
               f"{self.__tree_farm}"

    def get_tree_farm(self):
        return self.__tree_farm

    def add(self, tree: object) -> list:
        if tree:
            self.__tree_farm.append(tree)
            return self.__tree_farm
        else:
            raise TypeError("Passed 'tree' argument must be of class Tree and be an object.")

    def print_trees(self):
        for one_tree in self.__tree_farm:
            print(f"There is a {one_tree.get_species()} tree that is {one_tree.get_age()} years old.")

    def remove_tree(self, trunk_circumference: float):
        for one_tree in self.__tree_farm.copy():
            if trunk_circumference <= one_tree.get_circumference():
                print(f"You have harvested the {one_tree.get_species()} tree that is {one_tree.get_age()} old.")
                self.__tree_farm.remove(one_tree)
                return self.__tree_farm
        return None

    def remove_trees(self, trunk_circumference: float) -> list:
        for one_tree in self.__tree_farm.copy():
            if trunk_circumference <= one_tree.get_circumference():
                print(f"You have harvested the {one_tree.get_species()} tree that is {one_tree.get_age()} old.")
                self.__tree_farm.remove(one_tree)
        return self.__tree_farm


def main():
    tree1 = Tree("A", 1, 20)
    tree2 = Tree("B", 2, 40)
    tree3 = Tree("C", 3, 10)
    tree_farm1 = TreeFarm()
    tree_farm1.add(tree1)
    tree_farm1.add(tree2)
    tree_farm1.add(tree3)
    print(tree_farm1)
    tree_farm1.print_trees()
    tree_farm1.remove_trees(10)
    print(tree_farm1)
    tree_farm1.remove_tree(100)
    print(tree_farm1)


if __name__ == '__main__':
    main()
