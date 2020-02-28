import random
import copy
import doctest


def roll_die(number_of_rolls, number_of_sides):
    """Calculate the sum of the rolls of a die.

    This function simulates rolling a die a set number of times specified by the user and adding the results together
    to get the sum of the rolls. Returns the sum of the rolls.

    :param number_of_rolls: a positive non-zero integer.
    :param number_of_sides: a positive non-zero integer.
    :precondition: both parameters must be positive non-zero integers representing
                   # of rolls and # of sides respectively.
    :postcondition: returns a positive integer representing the sum of the rolls.
    :return: a positive non-zero integer.

    Computational thinking:
    Decomposed this problem into a single action; randomly choose an integer from 0 to max, then, store the value
    in a variable. This pattern is repeated a set number of times depending on how many rolls the user specifies.
    This process can be automated by using a while loop to repeat choosing a random integer a set number of times.
    The result is then returned back to the user as a integer.
    """
    sum_of_rolls = 0
    counter = 0
    while counter < number_of_rolls:
        result = random.randint(1, number_of_sides)
        sum_of_rolls += result
        counter += 1
    return sum_of_rolls


def movement_checker(character):
    """Upon movement, checks if user encounters monster if not heals character.

    :param character:
    :return:
    """
    monster_chance = roll_die(1, 4)
    if monster_chance == 1:
        return True
    else:
        if character['HP'][1] < character['HP'][0]:
            character['HP'][1] += 2
            print("no meet monsters, player current HP heal to %d" % (character['HP'][1]))
        else:
            print("your HP is full %d" % (character['HP'][1]))
        return False


def move_north(character):
    """Modifies character location to move North.

    :param character:
    :return:
    """
    if character['current_location'][1] == 1:
        print("You cannot go any more North! Turn back.")
        return False
    else:
        new_y = character['current_location'][1] - 1
        character['current_location'] = (character['current_location'][0], new_y)
        return True



def move_south(character):
    """Modifies character location to move South.

    :param character:
    :return:
    """
    if character['current_location'][1] == 5:
        print("You cannot go any more South! Turn back.")
        return False
    else:
        new_y = character['current_location'][1] + 1
        character['current_location'] = (character['current_location'][0], new_y)
        return True



def move_east(character):
    """Modifies character locaiton to move East.

    :param character:
    :return:
    """
    if character['current_location'][0] == 5:
        print("You cannot go any more East! Turn back.")
        return False

    else:
        new_x = character['current_location'][0] + 1
        character['current_location'] = (new_x, character['current_location'][1])
        return True



def move_west(character):
    """Modifies character location to move West.

    :param character:
    :return:
    """
    if character['current_location'][0] == 1:
        print("You cannot go any more West! Turn back.")
        return False
    else:
        new_x = character['current_location'][0] - 1
        character['current_location'] = (new_x, character['current_location'][1])
        return True



def grid_generator(character):
    """Generates a grid with current location and prints it to the user.
    :param character:
    :return:
    """
    x_coordinate = character['current_location'][0]
    y_coordinate = character['current_location'][1]
    for y, _ in enumerate(range(5), 1):
        line = ""
        for x, _ in enumerate(range(5), 1):
            if x == x_coordinate and y == y_coordinate:
                line += "[C]"
            else:
                line += "[ ]"
        print(line)

def generate_name():
    name = input("Please create player's name?")
    return name.capitalize().strip()


def select_class():
    class_list = ['barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk', 'paladin', 'ranger', 'rogue', 'sorcerer',
                  'warlock', 'wizard']
    for i, class_name in enumerate(class_list, 1):
        print(i, class_name)

    class_ask = input("Which class you want?(Please choose a number)").strip()
    return class_list[int(class_ask) - 1]


def select_race():
    race_list = ['dragonborn', 'dwarf', 'elf', 'gnome', 'half-elf', 'halfing', 'half-orc', 'human', 'tiefling']
    for i, race_name in enumerate(race_list, 1):
        print(i, race_name)
    race_ask = input("Which race you want?(Please choose a number)").strip()
    # while not race_ask.isdigit() or int(race_ask)> len(race_list) or int(race_ask) <= 0:
    #     race_ask = input("Please type a correct number: ").strip()
    return race_list[int(race_ask) - 1]


def create_character():
    character = {'Name': generate_name(), 'Class': select_class(), 'Race': select_race(), 'HP': [10, 10],
                 'current_location': (3, 3)}
    return character
    # else:
    #     print("the syllables must be a non-zero positive integer")
    #     return None

def print_character(character):
    """Use dictionary for loop to print each key and value horizontally

    Use for loop and object key and keys to print the values and keys in dictionary by order

    Computing Thinking:
    :Decomposition: Input a character dictionary and print out the understandable character's statue to players.
    :Pattern Matching and Data Representation: call the character's dictionary and use for loop and items() to print out
    each key and value
    :Abstraction and Generalization: print out the understandable character's statue to players
    :Algorithms and Automation: None
    :param character: invoke the return value from create_character function
    :precondition: the input must be a character dictionary
    :postcondition: First, print out a key. Second, print a colin. Third, print value. The print shows to  make player
    understand easily.
    """
    for key, value in character.items():
        print(key, ':', value)
    return None

def GIRD():
    # (1,1) , (2,1).....
    coord = {}
    for x in range(1, 6):
        for y in range(1, 6):
            coord[(y, x)] = ""
    print(coord)


def monster():
    monster_list = ['Gael(Katakan)', 'White Lady(Noonwraith)', 'Dragon(Forktail)', 'Melusine(Siren)', 'Morvudd(Fiend)',
                    'Jenny'
        , 'the Woods (Nightwraith)', 'Mourntart(Grave Hag)', 'Harrisi(Arachas)']
    mon_name = random.choice(monster_list)
    dic_monster = {'Name': mon_name, 'HP': [5, 5]}
    return dic_monster


def meet_monster(char):
    mon = monster()
    print("You meet a monster %s" % (mon['Name']))
    while True:
        decision = input("you have to choose fight or run?(type: run or fight)")
        if decision == "fight" or decision == "run":
            if decision == "fight":
                combat_round(char, mon)
            elif decision == "run":
                run(char)
            break


def run(char):
    decision_make = roll_die(1, 10)
    if decision_make == 1:
        print("you got attack")
        char['HP'][1] -= roll_die(1, 4)
        print("hit %s HP: %d" % (char['Name'], char['HP'][0] - char['HP'][1]))
        print("%s current HP: %d" % (char['Name'], char['HP'][1]))
    else:
        print("you successfully escape")


def combat_round(player, monster):
    count = 0
    while True:
        count += 1
        print("\nRound %d" % count)
        if attack(monster) <= 0:
            print("monster dead")
            return True
        elif attack(player) <= 0:
            print("you're dead")
            return False


def attack(hurt):
    hurt['HP'][1] -= roll_die(1, 6)
    print("hit %s HP: %d" % (hurt['Name'], hurt['HP'][0] - hurt['HP'][1]))
    print("%s current HP: %d" % (hurt['Name'], hurt['HP'][1]))
    return hurt['HP'][1]


def move_meet_monster(char):
    if movement_checker(char):
        meet_monster(char)
    # elif sud.movement_checker(char):
    #     pass


def main():
    doctest.testmod()
    print("Welcome to our wolf game!")
    char = create_character()
    print_character(char)

    while True:
        print(char['current_location'])
        grid_generator(char)
        user_movement = input("Where would you like to go? (n(north)/s(south)/e(east)/w(west)) (type q if you want to quit)")
        if char['HP'][1] <= 0 or user_movement == 'q':
            break
        else:
            if user_movement.lower().strip() == 'n':
                if move_north(char):
                    move_meet_monster(char)

            elif user_movement.lower().strip() == 'e':
                if move_east(char):
                    move_meet_monster(char)

            elif user_movement.lower().strip() == 's':
                if move_south(char):
                    move_meet_monster(char)

            elif user_movement.lower().strip() == 'w':
                if move_west(char):
                    move_meet_monster(char)
            else:
                print("That's not a valid input")
    # print(movement_checker({'name':'asdas','HP':[5,5]}))


if __name__ == '__main__':
    main()
