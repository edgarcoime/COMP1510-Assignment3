# Team Members: Tommy Chien, Edgar Coime
import random
import doctest
import boss_list


# Character movement and Grid events functions
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

    Doctest: Cannot doctest because of uses random module
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
    
    :param character: character is a dictionary containing name, class, race and HP.
    :return: Return False if the result of roll_die function is 1, others will justify if HP[1] < HP[0] add H[1]
             2 points and print the status or print out the full HP and return False

    Computational Thinking:
    This function is abstracted away from the character movement. This function can be decomposed into 2 steps: 1. Simu-
    late a die roll, 2. Check the die roll to see if its one, print the result to the user, and return True or False to
    indicate if the character has randomly encountered a monster in the arena. This function is responsible for
    generating a 25% chance of encountering a monster in the game and returns True or False to indicate if a monster
    has been found.

    Doctest: Cannot doctest because of uses random module
    """
    monster_chance = roll_die(1, 4)
    if monster_chance == 1:
        return True
    else:
        if character['HP'][1] < character['HP'][0]:
            character['HP'][1] += 2 if character['HP'][1] != (character['HP'][0] - 1) else 1
            print("The monsters couldn't catch up to you. This gives you the opportunity to bandage your wounds.\n"
                  f"You heal 2 points. You now have {character['HP'][1]}/{character['HP'][0]}HP\n")
        else:
            print("You were too fast for the onslaught of monsters. They couldn't catch you.\n"
                  f"You are in pretty good condition and don't need bandaging. "
                  f"You have {character['HP'][1]}/{character['HP'][0]}HP\n")
        return False


def boss_fight_checker(character, grid_events):
    """check the player could meet the boss or not by the location.
    
    :param character: character is a dictionary containing name, class, race and HP.
    :param grid_events: grid_events is a dictionary storing boss location
    :return: return the string of boss name if the current location match the boss location. Otherwise, return False

    Computational Thinking:
    This function is abstracted away from the character movement that checks and checks the current position against
    the grid_events param which indicates where the bosses are. This function cannot be decomposed any further as it
    is only responsible for checking current character location to see if the character encounters a boss. This function
    returns the key name that is associated with the boss, either 'dragon', 'giant', or 'wolf'.

    >>> grid_events = {'bosses': {(1, 1): 'dragon'}}
    >>> my_char = {'current_location': (1, 1)}
    >>> boss_fight_checker(my_char, grid_events)
    'dragon'

    >>> grid_events = {'bosses': {(3, 3): 'giant'}}
    >>> my_char = {'current_location': (3, 3)}
    >>> boss_fight_checker(my_char, grid_events)
    'giant'

    >>> grid_events = {'bosses': {(5, 5): 'wolf'}}
    >>> my_char = {'current_location': (5, 5)}
    >>> boss_fight_checker(my_char, grid_events)
    'wolf'

    >>> grid_events = {'bosses': {(1, 1): 'dragon'}}
    >>> my_char = {'current_location': (5, 5)}
    >>> boss_fight_checker(my_char, grid_events)
    False
    """
    if character['current_location'] in grid_events['bosses'].keys():
        if grid_events['bosses'][character['current_location']] == 'dragon':
            return 'dragon'
        elif grid_events['bosses'][character['current_location']] == 'giant':
            return 'giant'
        else:
            return 'wolf'
    else:
        return False


def move_north(character):
    """Modifies character location to move North.

    :param character: character is a dictionary containing name, class, race and HP.
    :precondition: character must be a dictionary contain key 'HP' and a a list for value get max HP and current HP by
                   the positive integers.
    :postcondition: if character's current location at y axis in 1, then print a warning message and return false.
                    Otherwise, create a tuple with subtracting 1 at y axis and return true.
    :return: return False if character meet the boundary or return true and create a new tuple to subtract one at
             character['current_location'][1]
    
    Computational thinking:
    To adapt the abstraction to solve this problem. Find the boundary of the map and try and error to show that it will
    go up at the map according to the addition or subtraction of x or y axis and give a error message if the target meet
    to the boundary.

    >>> my_char = {'current_location': (3, 2)}
    >>> move_north(my_char)
    True

    >>> my_char = {'current_location': (3, 1)}
    >>> move_north(my_char)
    The Northern wall of the colosseum towers before you.
    You cannot go any more North! Turn back.
    False
    """
    if character['current_location'][1] == 1:
        print("The Northern wall of the colosseum towers before you.\n"
              "You cannot go any more North! Turn back.")
        return False
    else:
        new_y = character['current_location'][1] - 1
        character['current_location'] = (character['current_location'][0], new_y)
        return True


def move_south(character):
    """Modifies character location to move South.

    :param character: character is a dictionary containing name, class, race and HP.
    :precondition: character must be a dictionary contain key 'HP' and a a list for value get max HP and current HP by
                   the
                   positive integers.
    :postcondition: if character's current location at y axis in 5, then print a warning message and return false.
                    Otherwise, create a tuple with add 1 at y axis and return true.
    :return: return False if character meet the boundary or return true and create a new tuple to add one at
             character['current_location'][1]
    
    Computational thinking:
    To adapt the abstraction to solve this problem. Find the boundary of the map and try and error to show that it will
    go up at the map according to the addition or subtraction of x or y axis and give a error message if the target meet
    to the boundary.

    >>> my_char = {'current_location': (3, 4)}
    >>> move_south(my_char)
    True

    >>> my_char = {'current_location': (3, 5)}
    >>> move_south(my_char)
    The Southern wall of the colosseum towers before you.
    You cannot go any more South! Turn back.
    False
    """
    if character['current_location'][1] == 5:
        print("The Southern wall of the colosseum towers before you.\n"
              "You cannot go any more South! Turn back.")
        return False
    else:
        new_y = character['current_location'][1] + 1
        character['current_location'] = (character['current_location'][0], new_y)
        return True


def move_east(character):
    """Modifies character location to move East.

    :param character: character is a dictionary containing name, class, race and HP.
    :precondition: character must be a dictionary contain key 'HP' and a a list for value get max HP and current HP by
                   the positive integers.
    :postcondition: if character's current location at x axis in 5, then print a warning message and return false.
                    Otherwise, create a tuple with add 1 at x axis and return true.
    :return: return False if character meet the boundary or return true and create a new tuple to add one at
             character['current_location'][0]
    
    Computational thinking:
    To adapt the abstraction to solve this problem. Find the boundary of the map and try and error to show that it will
    go up at the map according to the addition or subtraction of x or y axis and give a error message if the target meet
    to the boundary.

    >>> my_char = {'current_location': (4, 3)}
    >>> move_east(my_char)
    True

    >>> my_char = {'current_location': (5, 3)}
    >>> move_east(my_char)
    The Eastern wall of the colosseum towers before you.
    You cannot go any more East! Turn back.
    False
    """
    if character['current_location'][0] == 5:
        print("The Eastern wall of the colosseum towers before you.\n"
              "You cannot go any more East! Turn back.")
        return False
    else:
        new_x = character['current_location'][0] + 1
        character['current_location'] = (new_x, character['current_location'][1])
        return True


def move_west(character):
    """Modifies character location to move West.

    :param character: character is a dictionary containing name, class, race and HP.
    :precondition: character must be a dictionary contain key 'HP' and a a list for value get max HP and current HP by
                   the positive integers.
    :postcondition: if character's current location at x axis in 1, then print a warning message and return false.
                    Otherwise, create a tuple with subtract 1 at x axis and return true.
    :return: return False if character meet the boundary or return true and create a new tuple to subtract one at
             character['current_location'][0]
    
    Computational thinking:
    To adapt the abstraction to solve this problem. Find the boundary of the map and try and error to show that it will
    go up at the map according to the addition or subtraction of x or y axis and give a error message if the target meet
    to the boundary.

    >>> my_char = {'current_location': (2, 3)}
    >>> move_west(my_char)
    True

    >>> my_char = {'current_location': (1, 3)}
    >>> move_west(my_char)
    The Western wall of the colosseum towers before you.
    You cannot go any more West! Turn back.
    False
    """
    if character['current_location'][0] == 1:
        print("The Western wall of the colosseum towers before you.\n"
              "You cannot go any more West! Turn back.")
        return False
    else:
        new_x = character['current_location'][0] - 1
        character['current_location'] = (new_x, character['current_location'][1])
        return True


def grid_generator(character, grid_events):
    """Generates a grid with current location and prints it to the user.

    This function is responsible for creating a 5 by 5 grid which contains the character and the bosses in the game
    so that the user can visually see the data. It will also print out the legend for the symbols in the grid as well
    as the current HP of the character and how many bosses are still alive.
    
    :param grid_events: a valid dictionary that stores the events in the game and stores where they are located as
                        tuple coordinate points. This passed param must have the key 'bosses'.
    :param character: a dictionary that represents the user's character. This dictionary mut be a valid character
                      dictionary that has the character's 'Name' and 'HP' which is represented as a list.
    :precondition: character dictionary must be valid containing key value pairs for the character's stats. For
                   character param, key 'HP' must have a value that is a list and key 'current_location' must be a
                   5 by 5 coordinate point stored as a tuple. Param grid_events must have key value pair called 'bosses'
    :postcondition: this function returns nothing as it is only responsible for displaying the data in the parameters
                    in a legible way back to the user.
    :return: returns nothing, but displays the instructions for winning the game, a legend, and the grid for the user.

    Computational Thinking:
    This function abstracts away useless information in the character param and grid_events param and only prints the
    necessary information to progress through the game which include a win or lose condition. To display the grid
    dynamically a pattern emerges where each line must be printed sequentially until the desired number of rows is
    reached. This pattern can be achieved and automated through a nested for loop where the outer for-loop determines
    how many rows there are while the inner for-loop determines how many columns to print per row. From there printing
    the game elements can be easily done by using if and else statements for the character and the individual bosses.
    This function returns nothing but displays the necessary information to the user to properly progress and play the
    game.

    >>> my_char = {'Name': 'Jason', 'HP': [15, 15], 'current_location': (3, 3)}
    >>> grid_events = {'bosses': {(1, 1): 'dragon', (5, 1): 'giant', (5, 5): 'wolf'}}
    >>> grid_generator(my_char, grid_events)
    [C] = Your character named Jason
    [D] = Cetus the Dragon || [W] = Fenrir the Great Wolf || [G] = Ajax the Giant
    <BLANKLINE>
    [D][ ][ ][ ][G]
    [ ][ ][ ][ ][ ]
    [ ][ ][C][ ][ ]
    [ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][W]
    <BLANKLINE>
    You have 15HP
    3/3 bosses are still alive!
    You must kill them to be free of this nightmare!
    <BLANKLINE>
    """
    print(f"[C] = Your character named {character['Name']}\n"
          "[D] = Cetus the Dragon || [W] = Fenrir the Great Wolf || [G] = Ajax the Giant\n")
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
    print(f"\nYou have {character['HP'][1]}HP")
    print(f"{len(grid_events['bosses'].keys())}/3 bosses are still alive!\n"
          f"You must kill them to be free of this nightmare!\n")


def move_character(character):
    """Replace current character location with the new destination depending on the desired direction.
    
    This function acts like a control structure where depending on the user input it calls a helper function to
    calculate the desired new character location. The result of this helper function which will always be a tuple is
    stored returned back to the user.
    
    :param character: a dictionary that represents the user's character. This dictionary mut be a valid character
                      dictionary that has the character's 'Name' and 'HP'. The dictionary MUST have the key value pair
                      for current location where they key is 'current_location' and its value as a tuple.
    :precondition: the character param must be a valid dictionary and for the specific use case of this function
                   must have a key-value pair associated with the character location.
    :postcondition: this function returns the result the called helper function depending on the user input and will
                    always return a tuple.
    :return: the result of a helper function which is always a tuple representing a coordinate relative to a
             5 by 5 grid layout. If the user types 'q' or 'quit' returns a string 'q'.

    Computational Thinking:
    This function abstracts away the unnecessary information inside the character dictionary and isolates the
    'current_location' of the dictionary. The function is responsible for determining which helper function gets called
    to calculate the new coordinate relative to grid based on a North, South, East, West direction. This process can
    be automated using a while statement where the 4 if or elif statements are the compass directions, 1 elif statement
    is for 'quit' and the else statement is for invalid inputs. This function returns the result of the direction helper
    functions or 'q' to quit the game.

    Doctest: Cannot doctest because function requires user input
    """
    while True:
        user_prompt = input('Where would you like to move? Type: \n'
                            '"W" for [NORTH], "D" for [EAST], "S" for [SOUTH], "A" for [WEST]\n'
                            'To quit game type: Q or Quit\n')
        if user_prompt.lower().strip() == 'w':
            return move_north(character)

        elif user_prompt.lower().strip() == 'd':
            return move_east(character)

        elif user_prompt.lower().strip() == 's':
            return move_south(character)

        elif user_prompt.lower().strip() == 'a':
            return move_west(character)

        elif user_prompt.lower().strip() == 'q' or user_prompt.lower().strip() == 'quit':
            return "q"
        else:
            print("That's not a valid input")


# Character creator functions
def create_character():
    """Creates a valid character dictionary with the necessary properties to play the game

    :precondition: name input must be a string with Alphabet characters, your name cannot have integers or floats.
    :postcondition: this function returns a dictionary with the character's name, class, race, HP, and starting location
                    which is defaulted to the middle of the grid or coordinate (3, 3).
    :return: a character dictionary with the necessary properties to play and progress through the game.

    Computational Thinking:
    This function abstracts away selecting a class and race by refactoring it to other functions. This pattern of
    creating a character is very systematic and can be repeated over and over. This process can be automated by using
    dictionary literal syntax to call the key value pairs and calling the necessary helper functions to produce the
    desired value. This function returns a properly formatted and populated character dictionary that will allow
    the player to play through the game.

    Doctest: Cannot doctest because function requires user input
    """
    name = input("What was your name again? ").lower().capitalize().strip()
    character = {'Name': name,
                 'Class': select_class(),
                 'Race': select_race(),
                 'HP': [20, 20],
                 'current_location': (3, 3)}
    return character


def select_class():
    """Prompt user to choose from 12 classes.
    
    :precondition: user input must be a positive non-zero integer that is between 1 - 12 inclusive,
                   representing one of the twelve classes.
    :postcondition: if user chose a positive integer returns
                    a dictionary representing the class and attributes associated with it.
    :return: a dictionary representing the class name and the attributes of the class
    
    This function can be decomposed into two steps. First step being taking input from the user and the second being
    returning the appropriate class dictionary to reflect the user's choice.
    This process can be automated by initializing a dictionary with the key being the number associated with the class
    and the values being a dictionary of attributes that will be used to populate the character dictionary. This
    function returns a dictionary of values as well as the class name that can be used in create_character.

    Doctest: Cannot doctest because function requires user input
    """
    classes = {
        1: 'barbarian',
        2: 'bard',
        3: 'cleric',
        4: 'druid',
        5: 'fighter',
        6: 'monk',
        7: 'paladin',
        8: 'ranger',
        9: 'rogue',
        10: 'sorcerer',
        11: 'warlock',
        12: 'wizard',
    }
    print("\nTry to remember your class by choosing a number from 1-12!\n"
          "1. Barbarian: A fierce warrior of primitive background who can enter a battle rage.\n"
          "2. Bard: An inspiring magician whose powers echoes the music of creation.\n"
          "3. Cleric: A priestly champion who wields divine magic in service of a higher power.\n"
          "4. Druid: A priest of the Old Faith, wielding the powers of nature and adopting animal forms.\n"
          "5. Fighter: A master of martial combat, skilled with a variety of weapons and armor.\n"
          "6. Monk: A master of martial arts, harnessing the power of the body in pursuit of physical and spriritual "
          "perfection\n"
          "7. Paladin: A holy warrior bound to a sacred oath.\n"
          "8. Ranger: A warrior who combats threats on the edges of civilization.\n"
          "9. Rogue: A scoundrel who uses stealth and trickery to overcome obstacles and enemies.\n"
          "10. Sorcerer: A spellcaster who draws on inherent magic from a gift or bloodline.\n"
          "11. Warlock: A wielder of magic that is derived from a bargain with an extraplanar entity.\n"
          "12. Wizard: A scholarly magic-user capable of manipulating the structures of reality.\n")

    while True:
        user_class = input("What class did I specialize in again? ").strip()
        if user_class.isdigit() and int(user_class) in classes.keys():
            print(f"I was a {classes[int(user_class)].capitalize()}\n")
            return classes[int(user_class)]
        else:
            print("No, That's not the class that I was.\n"
                  "Please select a number from 1-12")


def select_race():
    """Prompt user to choose from 9 races.
    
    :precondition: user input must be a positive non-zero integer that is between 1 - 9 inclusive,
                   representing one of the nine races.
    :postcondition: returns a string representing the race of user has chosen.
    :return: a string representing a race.
    Computation thinking:
    This function can be decomposed into two steps. First step being taking input from the user and the second being
    returning the appropriate race name to reflect the user's choice.
    This process can be automated by initializing a dictionary with the key being the number associated with the race
    and the the value being race that has being chosen as a string. This function returns a the race name as a string
    which can be used in create_character.

    Doctest: Cannot doctest because function requires user input
    """
    races = {
        1: 'dwarf',
        2: 'elf',
        3: 'halfling',
        4: 'human',
        5: 'dragonborn',
        6: 'gnome',
        7: 'half-elf',
        8: 'half-orc',
        9: 'tiefling',
    }
    print("\nTry to remember your race by choosing a number from 1-9!\n"
          "1. Dwarf: Bold and hardy, dwarves are known as skilled warriors, miners, and workers of stone and metal.\n"
          "2. Elf: With their unearthly grace and fine features, elves appear hauntingly beautiful to humans and "
          "members of many other races.\n"
          "3. Halfling: The diminutive halflings survive in a world full of larger creatures by avoiding notice or, "
          "barring that, avoiding offense.\n"
          "4. Human: With their penchant for migration and conquest, humans are more physically diverse than other "
          "common races.\n"
          "5. Dragonborn: Dragonborn look very much like dragons standing erect in humanoid form, though they lack "
          "wings or a tail.\n"
          "6. Gnome: A gnome’s energy and enthusiasm for living shines through every inch of his or her tiny body.\n"
          "7. Halfelf: To humans, half-elves look like elves, and to elves, they look human.\n"
          "8. Halforc: Half-orcs’ grayish pigmentation, sloping foreheads, jutting jaws, prominent teeth, and towering"
          "builds make their orcish heritage plain for all to see.\n"
          "9. Tiefling: Tieflings are derived from human bloodlines, and in the broadest possible sense, they still "
          "look human.\n")

    while True:
        user_race = input("Where did I come from? and what was my background? ")
        if user_race.isdigit() and int(user_race) in races.keys():
            print(f"I was part of the {races[int(user_race)].capitalize()} race.\n")
            return races[int(user_race)]
        else:
            print("No, I am not of that race. I need to remember!\n"
                  "Please select a number from 1-9")


def print_character(character):
    """Display a structured and readable character info page by printing information back to the user.

    :param character: a dictionary that represents the user's character. This dictionary mut be a valid character
                      dictionary that has necessary key-value pairs associated with the character.
    :precondition: the passed dictionary must have key-value pairs for 'Name', 'Class', 'Race', and 'HP'. These values
                   must be properly formatted and be the correct data structure.
    :postcondition: this function returns nothing but prints out the information on the user's character.
    :return: nothing, but prints a stats sheet of the character.

    Computational Thinking:
    This function cannot be decomposed any further as its purpose is to format the character dictionary in a way that
    makes it more readable to the user. This process can be automated and processed by using f-string formatting
    to pass character's keys to print the dictionary's values. This function does not return or modify anything but it
    prints the character's dictionary in a formatted form.
    >>> my_char = {'Name': 'Jason', 'Class': 'barbarian', 'Race': 'human', 'HP': [15, 15], 'current_location': (3, 3)}
    >>> print_character(my_char)
    These are the characteristics that you remember.
    Name: Jason
    Hit-Points: 15/15
    Class: Barbarian
    Race: Human
    <BLANKLINE>
    <BLANKLINE>
    """
    print(  # basic character information
        f"These are the characteristics that you remember.\n"
        f"Name: {character['Name'].capitalize()}\n"
        f"Hit-Points: {character['HP'][0]}/{character['HP'][1]}\n"
        f"Class: {character['Class'].capitalize()}\n"
        f"Race: {character['Race'].capitalize()}\n\n")


def normal_battle(character):
    """Simulate a battle to the death with a monster.
    
    Choose a random monster name in a list and type fight or run to implement the functions to show the combat or
    escape. In the fighting part, show two types of results: defeat monster or monster defeat player. Finally, retype if
    the player didn't type fight or run correctly.

    :param character: character is a dictionary containing name, class, race and HP.
    :Precondition: character must be a dictionary contain key 'HP' and a a list for value get max HP and current HP by
                   the positive integers.
    :postcondition: Implement the combat_round while onster_dictionary['HP'][1] > 0 and character['HP'][1] > 0 if player
                   choose fight and break the while loop. Implement the retreat function if player choose run and break
                   the while loop. Otherwise, print a text and tell the player type again.
                   
    Computation thinking:
    Decompose the function into creating monster, asking player, typing correction and showing the result of combat or
    escaping. Make the abstraction to meet monster and show the process.

    Doctest: Cannot doctest because function requires user input and implements combat round which is reliant on the
             random module.
    """
    monster_names = ['Gael (Katakan)', 'White Lady (Noonwraith)', 'Forktail (Baby Wyvern)',
                     'Melusine (Siren)', 'Morvudd(Fiend)', 'The Woods (Nightwraith)',
                     'Mourntart (Grave Hag)', 'Harrisi (Arachas)']
    monster_name = random.choice(monster_names)
    monster_dictionary = {'Name': monster_name, 'HP': [5, 5]}
    print("You meet a monster named %s" % (monster_dictionary['Name']))
    while True:
        decision = input(f"You have {character['HP'][1]}HP and the enemy has {monster_dictionary['HP'][1]}\n"
                         "Will you fight or run? (type: fight or run):\n")
        if decision.strip().lower() == 'fight':
            while monster_dictionary['HP'][1] > 0 and character['HP'][1] > 0:
                combat_round(character, monster_dictionary)
            break
        elif decision.strip().lower() == 'run':
            retreat(character)
            break
        else:
            print("That is not a valid input please type 'run' or 'fight'")


def retreat(character):
    """Determine if character is backstabbed if retreat option is chosen.

    This function determines using a die roll whether or not the user's character is backstabbed in the process of
    running away from the monster. This chance is simulated using a die roll of 1d10, where 1 is the 10% chance that
    they do get hit while retreating.

    :param character: a dictionary that represents the user's character. This dictionary mut be a valid character
                      dictionary that has the character's 'Name' and 'HP' which is represented as a list.
    :precondition: character dictionary must be valid with the key value pairs of 'Name' and 'HP' mandatory inside the
                   dictionary.
    :postcondition: this function returns nothing but it modifies the character dictionary to reflect how much damage is
                    is inflicted if character is backstabbed.
    :return: no return value but modifies the 'character' param.
    """
    hit_chance_roll = roll_die(1, 10)
    print("You have a 10% chance of being backstabbed.")
    if hit_chance_roll == 1:
        retreat_damage = roll_die(1, 4)
        character['HP'][1] -= retreat_damage
        print("While retreating you are attacked from behind!\n"
              f"You are hit with {retreat_damage} damage, "
              f"leaving you with {character['HP'][1]}/{character['HP'][0]}HP.\n")
    else:
        print("You successfully escape!\n")


def combat_round(character, monster):
    """Simulate a single back and forth exchange between attacker and defender.

    This function acts as a control structure and print statement for the user to display helpful information
    for the story. This function keeps track of the current HP of the two dictionaries and decides whether another
    back and forth exchange should be done or a death screen should be displayed to the user to represent losing
    the game.

    :param character: a dictionary that represents the user's character. This dictionary mut be a valid character
                      dictionary that has the character's 'Name' and 'HP' which is represented as a list.
    :param monster: a dictionary that represents the minor monsters or non-boss monsters in the arena. This dictionary
                    must be a valid and have key value pairs that represents the monster's 'Name' and 'HP' represented
                    as a list.
    :precondition: both dictionaries must be valid with the key value pairs of 'Name' and 'HP' mandatory inside the
                   dictionary.
    :postcondition: this function returns nothing but it modifies the character and monster parameters to reflect how
                    much damage was done in the one for one exchange against each other.
    :return: no return value but modifies the 'character' param.

    Doctest: Cannot doctest because function implements the attack function which is reliant on the random module.
    """
    # Character attacks first
    print(f"{character['Name']} draws his weapon and lunges at the beast.")
    attack(character, monster)

    if 0 < monster['HP'][1]:
        print(f"{monster['Name']} staggers and recovers its composure. It glares at you and Retaliates!")
        attack(monster, character)
    else:
        print(f"You have successfully killed the monster {monster['Name']}!\n")

    # if character HP reaches 0 or lower death message shows
    if character['HP'][1] <= 0:
        print("You are dealt a fatal wound and everything turns black. All you hear are the monsters gathering \n"
              "around your body and the sound of your flesh being eaten.")


def attack(attacker, defender, times_attack=1, roll=1, side=6):
    """Calculate the amount of damage the defender receives depending on attacker damage rolls.
    
    This function calculates the total damage the defender receives from the attacker. This function takes 2
    necessary parameters which are the dictionaries of the attacker and defender. Damage is calculated based on a die
    roll system similar to DND and has 3 default parameters which assume a normal die roll of 1d6 rolled once.
    
    :param attacker: a dictionary that represents the attacker. This dictionary mut be a valid character dictionary that
                     has the attacker's 'Name' and 'HP' which is represented as a list.
    :param defender: a dictionary that represents the defender. This dictionary mut be a valid character dictionary that
                     has the defender's 'Name' and 'HP' which is represented as a list.
    :param times_attack: default value is 1, otherwise this param must be a non-zero positive integer. Represents
                         how many times the attacker attacks.
    :param roll: default value is 1, otherwise this param must be a non-zero positive integer. Represents how many times
                 the damage die is rolled to calculate a single attack.
    :param side: default value is 6, otherwise this param must be a non-zero positive integer. Represents how many sides
                 the damage die has.
    :precondition: both dictionaries must be valid with the key value pairs of 'Name' and 'HP' mandatory inside the
                   dictionary. The three default value parameters must be non-zero integers and SHOULD be imagined
                   and used as a die being rolled a certain amount of times with a certain number of sides.
    :postcondition: this function does not return anything but it modifies the defender parameter to reflect how much
                    damage was done to it.
    :return: no return value but modifies 'defender' param.

    Doctest: Cannot doctest because function implements the roll_die function which is reliant on the random module.
    """
    if times_attack == 1:
        damage_roll = roll_die(roll, side)
        defender['HP'][1] -= damage_roll
        print(f"{attacker['Name']} attacks {defender['Name']} and deals {damage_roll} damage.\n"
              f"Leaving {defender['Name']} with {defender['HP'][1]}/{defender['HP'][0]}HP.\n")
    else:
        damage_rolls = [roll_die(roll, side) for _ in range(times_attack)]
        damage_rolls_string = ', '.join(str(damage_roll) for damage_roll in damage_rolls)
        defender['HP'][1] -= sum(damage_rolls)
        print(
            f"{attacker['Name']} attacks with tremendous speed! Allowing it to strike {defender['Name']} "
            f"{times_attack} times.\n"
            f"{attacker['Name']} rolls {damage_rolls_string} for a total of {sum(damage_rolls)} damage. "
            f"Leaving {defender['Name']} with {defender['HP'][1]}/{defender['HP'][0]}HP.\n")


def boss():
    """Generate a boss dictionary for each of the bosses.

    Create three dictionaries to store in a dictionary as the values for the further usage of three_boss_fight function.

    precondition: none
    postcondition: return a dictionary with three string keys: 'dragon', 'giant' and 'wolf' ,and the respective values
                   are dragon, giant and wolf which have individual dictionaries.
    :return: return a dictionary with three string keys and values

    Computation thinking:
    We can use the data and pattern matching to use the same structure creating all the dictionaries below.
    >>> boss()
    {'dragon': {'Name': 'Cetus the Dragon', 'HP': [12, 12], 'side': 6, 'roll': 1, 'times': 1}, 'giant': {'Name': 'Ajax the Giant', 'HP': [8, 8], 'side': 8, 'roll': 1, 'times': 1}, 'wolf': {'Name': 'Fenrir the Great Wolf', 'HP': [8, 8], 'side': 4, 'roll': 1, 'times': 2}}
    """
    dragon = {"Name": "Cetus the Dragon", "HP": [12, 12], "side": 6, "roll": 1, "times": 1}
    giant = {"Name": "Ajax the Giant", "HP": [8, 8], "side": 8, "roll": 1, "times": 1}
    wolf = {"Name": "Fenrir the Great Wolf", "HP": [8, 8], "side": 4, "roll": 1, "times": 2}
    return {'dragon': dragon, 'giant': giant, 'wolf': wolf}


def three_boss_fight(character, boss_name, grid_events):
    """Simulate a battle to the death with one of the bosses of the game.

    Describe the whole process of boss by meeting three types of bosses: dragon, giant and wolf. Provide their
    background stories and their figures, and give the result of defeating boss or being defeated.

    :param character: a dictionary that represents the user's character. This dictionary mut be a valid character
                      dictionary that has the character's 'Name' and 'HP' which is represented as a list.
    :param boss_name: boss_name is a string containing dragon, giant or wolf
    :param grid_events: is a dictionary containing boss and its dictionary with their coordinates.
    :precondition: character must be a dictionary boss_name must be a string only accepting "dragon", "giant" or "wolf".
    :postcondition: Show the whole process of boss combat and give the result that who is the winner. Also, return a
                    new dictionary if player defeat a boss. Return false if player is been defeated.
    :return: return a new dictionary if the boss has been defeated and update the grid_events or return false if player
             is defeated by bosses.

    Computation thinking:
    Adapt the abstract to realize give the story and figure of coming boss and enter to the fight, showing the process
    of fight and deciding to continue or not according to the result of fight. Use decomposition to separate the
    helper functions and outside functions to implement the details. Finally, use pattern matching to make conditions
    to know is winning or losing.

    Doctest: Cannot doctest because function requires user input and implements 'attack' function which is reliant on
             the random module.
    """
    real_boss = boss()[boss_name]
    boss_list.call_monster(boss_name)
    boss_speech(boss_name)
    input(f"You are about to face one of the three bosses in this arena.\n"
          f"Prepare yourself as this is a battle to the death.\n"
          f"- press ENTER to continue -")
    while True:
        print(f"{character['Name']} draws his weapon and lunges at {real_boss['Name']}.")
        attack(character, real_boss)
        if real_boss['HP'][1] <= 0:
            new_dic = update_boss(boss_name, grid_events)
            congrats_for_winning(real_boss, grid_events)
            return new_dic
        print(f"{real_boss['Name']} staggers and recovers its composure. It glares at you and Retaliates!")
        attack(real_boss, character, real_boss['times'], real_boss['roll'], real_boss['side'])
        if character['HP'][1] <= 0:
            print("Your sight begins to blur as you feel you life fading away.\n"
                  "You have died. Please try again")
            return False


def update_boss(boss_name, grid_events):
    """Update the grid_events dictionary to delete boss key-value pair that was defeated

    the helper function to implement the delete the boss who is killed bt a player by its coordinate.
    create a copy to ensue not change the original data first and return a new dictionary.


    :param boss_name: boss_name is a string containing dragon, giant or wolf
    :param grid_events: is a dictionary containing boss and its dictionary with their coordinates.
    :precondition: boss_name must be a string containing dragon, giant or wolf.
                   grid_events must be a dictionary whose keys are "bosses" and the values are coordinates.
    :postcondition: if grid_events['bosses'] is not empty, show which boss the player defeat. Otherwise, print the
                    winning text to player.
    :return: return a new dictionary without the boss key and its value of the parameter boss_name.

    Computation thinking:
    Use abstract to search the word of boss that matches the boss the player meet and delete the boss the
    grid_events dictionary.

    >>> boss_name = 'dragon'
    >>> grid_events = {'bosses': {(1, 1): 'dragon', (5, 1): 'giant', (5, 5): 'wolf'}}
    >>> update_boss(boss_name, grid_events)
    {'bosses': {(5, 1): 'giant', (5, 5): 'wolf'}}

    >>> boss_name = 'giant'
    >>> grid_events = {'bosses': {(5, 1): 'giant', (5, 5): 'wolf'}}
    >>> update_boss(boss_name, grid_events)
    {'bosses': {(5, 5): 'wolf'}}

    >>> boss_name = 'wolf'
    >>> grid_events = {'bosses': {(5, 5): 'wolf'}}
    >>> update_boss(boss_name, grid_events)
    {'bosses': {}}
    """
    new_dic = grid_events.copy()
    for coordinate in new_dic['bosses'].keys():
        if new_dic['bosses'][coordinate] == boss_name:
            del new_dic['bosses'][coordinate]
            return new_dic


def congrats_for_winning(real_boss, grid_events):
    """Display victory speech if the game is won or defeat/death speech if you have lost the game.

    Create the helper function to figure out is just only kill one of bosses or achieving the goal of wining which is
    defeating whole three bosses.


    :param real_boss: be a dictionary under the function boss() containing the details of bosses
    :param grid_events: is a dictionary containing boss and its dictionary with their coordinates.
    :precondition: real_boss must be a dictionary whose keys are "Name" and the values are the name of bosses.
    :postcondition: if grid_events['bosses'] is not empty, show which boss the player defeat. Otherwise, print the
                    winning text to player.

    Computation thinking:
    Use thee pattern match to make the condition to separate the win or defeating a boss.

    >>> dragon = {"Name": "Cetus the Dragon", "HP": [12, 12], "side": 6, "roll": 1, "times": 1}
    >>> grid_events = {'bosses': {(5, 1): 'giant', (5, 5): 'wolf'}}
    >>> congrats_for_winning(dragon, grid_events)
    Congratulations! You have beaten Cetus the Dragon
    You can now proceed to the other bosses in the arena.

    >>> wolf = {"Name": "Fenrir the Great Wolf", "HP": [8, 8], "side": 4, "roll": 1, "times": 2}
    >>> grid_events = {'bosses': {}}
    >>> congrats_for_winning(dragon, grid_events)
    As you stand before the lifeless carcass of Cetus the Dragon the final champion.
    You take a deep breath as you are overcome with the elation of escaping this nightmarish arena.
    You breath in the last breath of air that you will take in this God forsaken place and look forward
    to your new reborn life.
    Thank you so much to play our game. Tha game producers are Edgar and Tommy
    """
    if grid_events['bosses'] != {}:
        print(f"Congratulations! You have beaten {real_boss['Name']}\n"
              "You can now proceed to the other bosses in the arena.")
    else:
        print(f"As you stand before the lifeless carcass of {real_boss['Name']} the final champion.\n"
              "You take a deep breath as you are overcome with the elation of escaping this nightmarish arena.\n"
              "You breath in the last breath of air that you will take in this God forsaken place and look forward\n"
              "to your new reborn life.\n"
              "Thank you so much to play our game. Tha game producers are Edgar and Tommy")


def boss_speech(choice):
    """Display unique Boss introduction when encountering each of the bosses in the arena.

    a helper function to show the detail description for each boss by boss's name

    :param choice: be a string only covering "dragon","giant" and "wolf"
    :precondition: choice must be a string only covering "dragon","giant" and "wolf"
    :postcondition: print out the text according the boss name the player meet.

    Computation thinking:
    Use thee pattern match to make the condition to show which is going to show in three_boss_fight function.
    >>> boss_speech('giant')
    As you approach the Giant named Ajax his lips begin to curl upward as his monstrous body towers
    before you. His club is the length and seems to weigh as much as he does; yet, he swings the club
    effortlessly. You take a deep breath as you ready yourself for battle while Ajax laughs condescendingly.
    <BLANKLINE>
    You have challenged Ajax the Giant, one of the three champions in this arena.
    His size gives him abnormal strength allowing him an attack of 1d8, his size gives him above average 8HP.
    >>> boss_speech('wolf')
    Fenrir stares at you as if he was looking at a rabbit that he could kill at any moment. From a
    distance you can already tell that he was leagues above being just 'nimble'. He was fast and with
    ferocity to match that speed as well. You prepare yourself sharpening your instincts as it approaches.
    <BLANKLINE>
    You have challenged Fenrir the Great Wolf, one of the three champions in this arena.
    His speed allows him to attack twice with a roll of 1d4, compared to the others he is still fragileso he has average health of 6HP

    """
    if choice == "dragon":
        print("You have woken the Dragon named Cetus. As it approaches you, you fight off the urge to run\n"
              "away from the nightmarish beast in front of you clad with dark obsidian scales. As Cetus approaches\n"
              "its mouth begins to froth with molten magma and his nostrils flair and emit steam. You take up arms\n"
              "and ready yourself mentally and physically for battle that will unfold.\n")
        print("You have challenged Cetus the Dragon, one of the three champions in this arena.\n"
              "His claws give it high attack of 2d4, and his draconic scales give him 12HP ")
    elif choice == "giant":
        print("As you approach the Giant named Ajax his lips begin to curl upward as his monstrous body towers\n"
              "before you. His club is the length and seems to weigh as much as he does; yet, he swings the club\n"
              "effortlessly. "
              "You take a deep breath as you ready yourself for battle while Ajax laughs condescendingly.\n")
        print("You have challenged Ajax the Giant, one of the three champions in this arena.\n"
              "His size gives him abnormal strength allowing him an attack of 1d8, "
              "his size gives him above average 8HP.")
    else:
        print("Fenrir stares at you as if he was looking at a rabbit that he could kill at any moment. From a\n"
              "distance you can already tell that he was leagues above being just 'nimble'. He was fast and with\n"
              "ferocity to match that speed as well. "
              "You prepare yourself sharpening your instincts as it approaches.\n")
        print("You have challenged Fenrir the Great Wolf, one of the three champions in this arena.\n"
              "His speed allows him to attack twice with a roll of 1d4, compared to the others he is still fragile"
              "so he has average health of 6HP")


def main():
    doctest.testmod()
    grid_events = {
        'bosses': {(1, 1): 'dragon',
                   (5, 1): 'giant',
                   (5, 5): 'wolf'},
        'events': None
    }

    # GAME STARTS HERE

    # INTRODUCTION AND PRELUDE TO FIGHTING IN ARENA
    print(  # introduction upon waking up
        "You wake up to the sound of the prison cell creaking. Your head throbs with pain as you try to regain your \n"
        "senses and remember what happened to you. Before you can collect your thoughts, you are interrupted by the \n"
        "laughter from behind you. \n"
        "    Death row inmate: 'Hahaha . . . You are going into the arena tomorrow. Only death awaits you there.'\n"
    )
    input("You have no idea what is going on and you wonder what this ‘arena’ is, so you ask the man for more "
          "details.\n "
          "- press ENTER to continue -")
    print(
        "    Death row inmate: 'The arena is where the king throws inmates to fight his 3 champions. \n"
        "                       Ajax the Giant, Fenrir the great Wolf, and Cetus the Dragon.\n"
        "                       You stand no chance. You are going to be slaughtered!'\n"
    )

    while True:
        print("Fear grips you, but if you are fighting tomorrow you need to know who you will be fighting. "
              "You ask him . . .")
        intro_q1 = input("Choose a number from 1-4 to ask the man a question.\n"
                         "1. Who is Ajax the Giant?\n"
                         "2. Who is Fenrir the Great Wolf?\n"
                         "3. Who is Cetus the Dragon?\n"
                         "4. What happens if I win against them?\n")
        if intro_q1.isdigit() and int(intro_q1) == 1:
            print("    Death row inmate: 'Ajax the Giant is a Troll who stands as tall as three adult men.\n"
                  "                       He can single handily crush you with a swing of his club.'\n")
        elif intro_q1.isdigit() and int(intro_q1) == 2:
            print("    Death row inmate: 'Fenrir the Great Wolf is a fierce beast whose speed is unrivaled in battle\n"
                  "                       in the time it takes you to land a hit he would've striked you twice.'\n")
        elif intro_q1.isdigit() and int(intro_q1) == 3:
            print("    Death row inmate: 'Cetus the Dragon has served in the king's bloodline for\n"
                  "                       thousands of years. His ferociousness is otherworldly and his thick hide\n"
                  "                       protects him from weapons that would pierce even walls'\n")
        elif intro_q1.isdigit() and int(intro_q1) == 4:
            print("    Death row inmate: 'HAHAHA You are never going to win, not even in a thousand years. But if \n"
                  "                       you do manage to pull a miracle the king will set you free with fortunes\n"
                  "                       that the Gods would even kill for.'\n")
            break
        else:
            print("That's not a valid choice. Type a number associated with a choice.\n")
    print("You end the conversation and try to get some sleep. Trying to remember who you are.\n"
          "You ask yourself:")

    my_char = create_character()
    # my_char = {
    #     'Name': 'Edgar',
    #     'Class': 'barbarian',
    #     'Race': 'human',
    #     'HP': [15, 40],
    #     'current_location': (3, 3)}
    # print_character(my_char)

    input("You close your eyes to rest hoping that this is all a ridiculous nightmare.\n"
          "- press ENTER to continue -")

    print("You wake up to the sound of the screaming crowd as you stagger to your feet. You are in the arena\n"
          "and monsters surround you on all sides. You remember the What the old man said. . .\n"
          "To get out of here I must kill the three champions of this ARENA!\n")

    while my_char['HP'][1] > 0 and grid_events['bosses']:
        # print(my_char['current_location'])
        # print(grid_events)
        grid_generator(my_char, grid_events)
        quit_prompt = move_character(my_char)
        if quit_prompt == 'q':
            print("Thanks for playing our game! Please play again next time.")
            break
        elif quit_prompt:
            boss_fight = boss_fight_checker(my_char, grid_events)
            monster_battle = movement_checker(my_char)
            if boss_fight:
                if boss_fight == 'dragon':
                    grid_events = three_boss_fight(my_char, boss_fight, grid_events)
                elif boss_fight == 'giant':
                    grid_events = three_boss_fight(my_char, boss_fight, grid_events)
                else:
                    grid_events = three_boss_fight(my_char, boss_fight, grid_events)
            else:
                if monster_battle:
                    print("A monster catches up to you. Get ready for battle!")
                    normal_battle(my_char)
        else:
            pass


if __name__ == '__main__':
    main()
