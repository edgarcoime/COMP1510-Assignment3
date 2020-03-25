import doctest


class Tree:

    def __init__(self, species: str, age: int, circumference: float):
        """Initialize a tree object with the attributes species, age, and circumference.

        :param species: a string that contains the Tree's species name. Must not be just whitespace or empty.
        :param age: an integer that represents the Tree's age in years. This cannot be a negative number as there is
                    no such thing as negative age.
        :param circumference: a float that represents the Tree's total circumference in centimetres. This value
                              cannot equal a negative or zero.
        :precondition: parameters must make logical sense with respect to trees. Name cannot be an empty string or just
                       contain whitespace. Age must be an integer that represents age in years so it cannot be a
                       negative number. Circumference must equal the circumference of the tree and be represented as a
                       float value.
        :postcondition: instantiates an object in memory, initializing it with the attributes of species, age, and
                        circumference.
        :raise ValueError: error is raised when the passed arguments do not follow the param guidelines and the
                           precondition.

        >>> maple = Tree("Maple", 150, 50.23)
        """
        if "".join(letter for letter in species if letter.isalpha()) == "":
            raise ValueError("The species name cannot be empty or only be whitespace!")
        else:
            self.__species = species.title()
        if age < 0:
            raise ValueError("The tree cannot have negative age.")
        else:
            self.__age = age
        if circumference < 0:
            raise ValueError("The tree cannot have a negative circumference.")
        self.__circumference = circumference

    def __str__(self):
        """Define the string representation of the object is.

        :postcondition: Returns a detailed overview of the Tree object containing its attributes of species, age, and
                        circumference.
        :return: a string containing the details of the Tree object such as its species, age, and circumference.

        >>> maple = Tree("Maple", 150, 50.23)
        >>> print(maple)
        This is a Maple tree that is 150 years old and has a circumference of 50.23 centimetres.
        """
        return f"This is a {self.__species} tree that is {self.__age} years old and has a circumference of " \
               f"{self.__circumference} centimetres."

    def __repr__(self):
        """Define what the object representation of this object will be as an expression.

        :postcondition: returns the object representation of this Tree object as a valid python expression.
        :return: a string that represents the object representation of the Tree class.

        >>> maple = Tree("Maple", 150, 50.23)
        >>> print(maple.__repr__())
        Tree("Maple", 150, 50.23)
        """
        return f'Tree("{self.__species}", {self.__age}, {self.__circumference})'

    def get_species(self):
        """Retrieve the string value of this Tree's species name.

        :postcondition: returns the Tree's species name as a string in title case that is stored in __species.
        :return: a string indicating the Tree's species name.

        >>> maple = Tree("Maple", 150, 50.23)
        >>> maple.get_species()
        'Maple'
        """
        return self.__species

    def get_age(self):
        """Retrieve the integer value of this Tree's age.

        :postcondition: returns the Tree's age as a string in the unit of years which is stored in the attribute __age.
        :return: an integer that represents the Tree's age.

        >>> maple = Tree("Maple", 150, 50.23)
        >>> maple.get_age()
        150
        """
        return self.__age

    def get_circumference(self):
        """Retrieve the float value of this Tree's total circumference.

        :postcondition: returns the Tree's circumference as a float that is in the unit of centimetres which is found
                        in the attribute __circumference.
        :return: a float that represents the tree's total circumference in centimetres.

        >>> maple = Tree("Maple", 150, 50.23)
        >>> maple.get_circumference()
        50.23
        """
        return self.__circumference


def main():
    doctest.testmod()
    maple = Tree("mApLe", 245, 189.34)
    print(maple)
    print(maple.__repr__())


if __name__ == "__main__":
    main()
