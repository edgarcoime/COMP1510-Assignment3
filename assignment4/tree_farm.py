import doctest
import assignment4
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

    def add(self, tree: object):
        """Add a class object of Tree into this TreeFarm object's list found under the attribute __tree_farm.

        :param tree: an object that must be an instance of the class 'Tree' that has the attributes of species, age,
                     and circumference.
        :precondition: the param tree must be of the 'Tree' type class that contains the attributes of species, age,
                       and circumference otherwise a type error will be raised.
        :postcondition: modifies the __tree_farm attribute in this class object and appends a 'Tree' class object into
                        the list.
        :raise TypeError: error is raised if the passed argument is not an instance of the 'Tree' class.
        :return: returns nothing as it modifies the __tree_farm attribute by appending a new 'Tree' class object.

        >>> tree_farm = TreeFarm()
        >>> tree1 = Tree("Oak", 245, 211)
        >>> tree_farm.add(tree1)
        >>> print(tree_farm)
        [Tree("Oak", 245, 211)]
        """
        if isinstance(tree, assignment4.tree.Tree):
            self.__tree_farm.append(tree)
            return self.__tree_farm
        else:
            raise TypeError("Passed 'tree' argument must be of class Tree and be an object.")

    def print_trees(self):

        """Print all the trees in the __tree_farm list including the species name and its age.

        :postcondition: prints a descriptive string of the each tree in the tree_farm list which includes its species
                        name and its age.
        :return: returns nothing but prints a description of each tree contained in the tree_farm list.

        >>> tree_farm = TreeFarm()
        >>> tree1 = Tree("Oak", 245, 211)
        >>> tree2 = Tree("Maple", 111, 245)
        >>> tree_farm.add(tree1)
        >>> tree_farm.add(tree2)
        >>> tree_farm.print_trees()
        These are the trees in the tree farm:
        There is a Oak tree that is 245 years old.
        There is a Maple tree that is 111 years old.
        """
        print("These are the trees in the tree farm:")
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
    doctest.testmod()
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
