class Tree:
    def __init__(self, species: str, age: int, trunk_circumference: float):
        self.species = species.strip()
        self.age = age
        self.trunk_circumference = trunk_circumference
        if species.strip() == "":
            raise ValueError("species cannot be empty.")
        if age < 0:
            raise ValueError("Tree's age cannot be negative.")
        if trunk_circumference < 0:
            raise ValueError("Tree's trunk circumference cannot be negative.")

    def __repr__(self):
        return f"The tree is {self.species},and its age and its circumference are {self.age} and {self.trunk_circumference} cm."

    def __str__(self):
        return f"The tree is {self.species},and its age and its circumference are {self.age} and {self.trunk_circumference} cm."

    def get_species(self):
        return self.species

    def get_age(self):
        return self.age

    def get_trunk_circumference(self):
        return self.trunk_circumference


def main():
    tree2 = Tree("A", 40, 30)
    print(tree2)
    try:
        tree1 = Tree("A", -1, 30)
    except ValueError:
        print("Get error")
        return tree1




if __name__ == '__main__':
    main()
