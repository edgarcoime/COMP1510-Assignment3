import random
import copy
import doctest


# global variables to mark events


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
        return False


def move_north(character):
    """Modifies character location to move North.

    :param character:
    :return:
    """
    if character['current_location'][1] == 1:
        print("The Northern wall of the colosseum towers before you.\n"
              "You cannot go any more North! Turn back.")
    else:
        new_y = character['current_location'][1] - 1
        character['current_location'] = (character['current_location'][0], new_y)


def move_south(character):
    """Modifies character location to move South.

    :param character:
    :return:
    """
    if character['current_location'][1] == 5:
        print("The Southern wall of the colosseum towers before you.\n"
              "You cannot go any more South! Turn back.")
    else:
        new_y = character['current_location'][1] + 1
        character['current_location'] = (character['current_location'][0], new_y)


def move_east(character):
    """Modifies character locaiton to move East.

    :param character:
    :return:
    """
    if character['current_location'][0] == 5:
        print("The Eastern wall of the colosseum towers before you.\n"
              "You cannot go any more East! Turn back.")
    else:
        new_x = character['current_location'][0] + 1
        character['current_location'] = (new_x, character['current_location'][1])


def move_west(character):
    """Modifies character location to move West.

    :param character:
    :return:
    """
    if character['current_location'][0] == 1:
        print("The Western wall of the colosseum towers before you.\n"
              "You cannot go any more West! Turn back.")
    else:
        new_x = character['current_location'][0] - 1
        character['current_location'] = (new_x, character['current_location'][1])


def grid_generator(character, grid_events):
    """Generates a grid with current location and prints it to the user.

    :param character:
    :return:
    """
    for y, _ in enumerate(range(5), 1):
        line = ""
        for x, _ in enumerate(range(5), 1):
            if (x, y) == character['current_location']:
                line += "[C]"
            elif (x, y) in grid_events['bosses'].keys():
                if grid_events['bosses'][(x, y)] == 'dragon':
                    line += "[D]"
                elif grid_events['bosses'][(x, y)] == 'wolf':
                    line += "[W]"
                elif grid_events['bosses'][(x, y)] == 'giant':
                    line += "[G]"
                else:
                    pass
            else:
                line += "[ ]"
        print(line)


def move_character(character, grid_events):
    user_movement = input('Where would you like to move?\n'
                          'type (N or North) - (E or East) - (S or South) - (W or West)\n')
    if user_movement.lower().strip() == 'n':
        move_north(character)
    elif user_movement.lower().strip() == 'e':
        move_east(character)
    elif user_movement.lower().strip() == 's':
        move_south(character)
    elif user_movement.lower().strip() == 'w':
        move_west(character)
    else:
        print("That's not a valid input")


def main():
    doctest.testmod()
    GRID_EVENTS = {
        'bosses': {(1, 1): 'dragon',
                   (5, 1): 'giant',
                   (5, 5): 'wolf'},
        'events': None
    }
    char = {
        'current_location': (3, 3),
        'HP': [10, 1]
    }

    while char['HP'][1] != 0 and GRID_EVENTS['bosses']:
        print(char['current_location'])
        grid_generator(char, GRID_EVENTS)
        move_character(char, GRID_EVENTS)


if __name__ == '__main__':
    main()
