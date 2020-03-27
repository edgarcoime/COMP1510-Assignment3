import assignment4
from assignment4.tree import Tree
import doctest


class TreeFarm:

    def __init__(self):
        """Initialize a TreeFarm object with the attribute of an empty list.

        :postcondition: instantiates an object in memory, initializing it with the attribute of __tree_farm that
                        contains an empty list

        >>> tree_farm = TreeFarm()
        """
        self.__tree_farm = []

    def __str__(self):
        """Define the string representation of the TreeFarm class object.

        :postcondition: returns a detailed string representation of the tree_farm object that is in the form of a list
                        and what it contains.
        :return: a string that depicts a list that contains the string representation of the elements found within the
                 the tree_farm object.

        >>> tree_farm = TreeFarm()
        >>> print(tree_farm)
        []
        """
        return f"{self.__tree_farm}"

    def __repr__(self):
        """Define what the object representation of this object will be as an expression.

        :postcondition: returns the object representation of this tree_farm object a valid python expression.
        :return: a string that represents the object representation of TreeFarm class.

        >>> tree_farm = TreeFarm()
        >>> print(tree_farm.__repr__())
        TreeFarm():
        []
        """
        return f"TreeFarm():\n" \
               f"{self.__tree_farm}"

    def get_tree_farm(self):
        """Retrieve the list value found in this TreeFarm's __tree_farm attribute.

        :postcondition: returns the list containing the tree objects found in this TreeFarm's tree_farm attribute.
        :return: a list that displays the Tree classes found in this object.

        >>> tree_farm = TreeFarm()
        >>> tree_farm.get_tree_farm()
        []
        """
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
        """Remove a tree from the list in __tree_farm that is equal to or greater than the measurement passed.

        :param trunk_circumference: a float indicating the minimum circumference required by the user.
        :precondition: param must be a Number that has been converted into a circumference from the diameter which
                       indicates how much wood the user wants.
        :postcondition: returns the 'Tree' object that has been removed from the __tree_farm list attribute.
        :return: return an object that is of type 'Tree' indicating the Tree that has been removed.

        >>> tree_farm = TreeFarm()
        >>> tree1 = Tree("Oak", 245, 211)
        >>> tree_farm.add(tree1)
        >>> print(tree_farm.remove_tree(200))
        This is a Oak tree that is 245 years old and has a circumference of 211 centimetres.
        """
        for one_tree in self.__tree_farm.copy():
            if trunk_circumference <= one_tree.get_circumference():
                # print(f"You have harvested the {one_tree.get_species()} tree that is {one_tree.get_age()} years old.")
                self.__tree_farm.remove(one_tree)
                return one_tree

    def remove_trees(self, trunk_circumference: float):
        """Remove trees from the list in __tree_farm that is equal to or greater than the measurement passed

        :param trunk_circumference: a float indicating the minimum circumference required by the user.
        :precondition: param must be a Number that has been converted into a circumference from the diameter which
                       indicates how much wood the user wants.
        :postcondition: returns a list of 'Tree' objects that have been removed from the __tree_farm list attribute.
        :return: return a list of objects that is of type 'Tree' which represent the trees that have been removed
                 from the __tree_farm list.

        >>> tree_farm = TreeFarm()
        >>> tree1 = Tree("Oak", 245, 211)
        >>> tree2 = Tree("Maple", 245, 125)
        >>> tree_farm.add(tree1)
        >>> tree_farm.add(tree2)
        >>> print(tree_farm.remove_trees(100))
        [Tree("Oak", 245, 211), Tree("Maple", 245, 125)]
        """
        removed_trees = []
        for one_tree in self.__tree_farm.copy():
            if trunk_circumference <= one_tree.get_circumference():
                # print(f"You have harvested the {one_tree.get_species()} tree that is {one_tree.get_age()} years old.")
                removed_trees.append(one_tree)
                self.__tree_farm.remove(one_tree)
        return removed_trees


def main():
    doctest.testmod()


if __name__ == '__main__':
    main()
