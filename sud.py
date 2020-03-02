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
            print("The monsters couldn't catch up to you. This gives you the opportunity to bandage your wounds.\n"
                  f"You heal 2 points. You now have {character['HP'][1]}/{character['HP'][0]}HP\n")
        else:
            print("You were too fast for the onslaught of monsters. They couldn't catch you.\n"
                  f"You are in pretty good condition and don't need bandaging. "
                  f"You have {character['HP'][1]}/{character['HP'][0]}HP\n")
        return False


def boss_fight_checker(character, grid_events):
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
    :param grid_events:
    :param character:
    :return:
    """
    print(f"[C] Is your character named {character['Name']}\n"
          "[D] = Cetus the Dragon || [W] = Fenrir the Great Wolf || [G] = Ajax the Giant")
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
    print(f"You have {character['HP'][1]}HP")
    print(f"{len(grid_events['bosses'].keys())}/3 bosses are still alive!\n"
          f"You must kill them to be free of this nightmare!\n")


def move_character(character):
    while True:
        user_prompt = input('Where would you like to move?\n'
                            'type (N or North) - (E or East) - (S or South) - (W or West)\n'
                            'To quit game type: Q or Quit\n')
        if user_prompt.lower().strip() == 'n' or user_prompt.lower().strip() == 'north':
            move_north(character)
            break
        elif user_prompt.lower().strip() == 'e' or user_prompt.lower().strip() == 'east':
            move_east(character)
            break
        elif user_prompt.lower().strip() == 's' or user_prompt.lower().strip() == 'south':
            move_south(character)
            break
        elif user_prompt.lower().strip() == 'w' or user_prompt.lower().strip() == 'west':
            move_west(character)
            break
        elif user_prompt.lower().strip() == 'q' or user_prompt.lower().strip() == 'quit':
            return True
        else:
            print("That's not a valid input")


# Character creator functions
def create_character():
    character = {'Name': generate_name(),
                 'Class': select_class(),
                 'Race': select_race(),
                 'HP': [15, 15],
                 'current_location': (3, 3)}
    return character


def generate_name():
    name = input("What was your name again? ")
    return name.lower().capitalize().strip()


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

    classes_prompt = True
    while classes_prompt:
        user_class = int(input("What class did I specialize in again? "))
        if user_class in classes.keys():
            print(f"I was a {classes[user_class].capitalize()}\n")
            classes_prompt = False
            return classes[user_class]
        else:
            print("No, That's not the class that I was.\n"
                  "Please select a number from 1-12")


def select_race():
    """Prompt user to choose from 9 races.
    :precondition: user input must be a positive non-zero integer that is between 1 - 9 inclusive,
                   representing one of the nine races.
    :postcondition: returns a string representing the race of user has chosen.
    :return: a string representing a race.
    This function can be decomposed into two steps. First step being taking input from the user and the second being
    returning the appropriate race name to reflect the user's choice.
    This process can be automated by initializing a dictionary with the key being the number associated with the race
    and the the value being race that has being chosen as a string. This function returns a the race name as a string
    which can be used in create_character.
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

    race_prompt = True
    while race_prompt:
        user_race = int(input("Where did I come from? and what was my background? "))
        if user_race in races.keys():
            print(f"I was part of the {races[user_race].capitalize()} race.\n")
            race_prompt = False
            return races[user_race]
        else:
            print("No, I am not of that race. I need to remember!\n"
                  "Please select a number from 1-9")


def print_character(character):
    print(  # basic character information
        f"These are the characteristics that you remember.\n"
        f"Name: {character['Name'].capitalize()}\n"
        f"Hit-Points: {character['HP'][0]}/{character['HP'][1]}\n"
        f"Class: {character['Class'].capitalize()}\n"
        f"Race: {character['Race'].capitalize()}\n\n")


def normal_battle(character):
    monster = create_monster()
    print("You meet a monster named %s" % (monster['Name']))
    while monster['HP'][1] > 0 and character['HP'][1] > 0:
        decision = input(f"You have {character['HP'][1]}HP and the enemy has {monster['HP'][1]}\n"
                         "Will you fight or run? (type: fight or run):\n")
        if decision == 'fight':
            combat_round(character, monster)
        elif decision == 'run':
            retreat(character)
            break
        else:
            pass


def create_monster():
    monster_names = ['Gael (Katakan)',
                     'White Lady (Noonwraith)',
                     'Forktail (Baby Wyvern)',
                     'Melusine (Siren)',
                     'Morvudd(Fiend)',
                     'The Woods (Nightwraith)',
                     'Mourntart (Grave Hag)',
                     'Harrisi (Arachas)']
    monster_name = random.choice(monster_names)
    monster_dictionary = {'Name': monster_name, 'HP': [5, 5]}
    return monster_dictionary


def retreat(character):
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
    if times_attack == 1:
        damage_roll = roll_die(roll, side)
        defender['HP'][1] -= damage_roll
        print(f"{attacker['Name']} attacks {defender['Name']} and deals {damage_roll} damage.\n"
              f"Leaving {defender['Name']} with {defender['HP'][1]}/{defender['HP'][0]}HP.\n")
    else:
        damage_rolls = []
        damage_string = ""
        for _ in range(times_attack):
            damage_roll = roll_die(roll, side)
            damage_rolls.append(damage_roll)
            damage_string += str(damage_roll) + ", "
        defender['HP'][1] -= sum(damage_rolls)
        print(
            f"The beast attacks with tremendous speed! Allowing it to strike {defender['Name']} {times_attack} times.\n"
            f"{attacker['Name']} rolls {damage_string}for a total of {sum(damage_rolls)} damage. "
            f"Leaving {defender['Name']} with {defender['HP'][1]}/{defender['HP'][0]}HP.\n")


def boss():
    dragon = {"Name": "dragon", "HP": [20, 20], "side": 4, "roll": 2, "times": 1}
    giant = {"Name": "giant", "HP": [15, 15], "side": 12, "roll": 1, "times": 1}
    wolf = {"Name": "wolf", "HP": [12, 12], "side": 6, "roll": 1, "times": 2}
    return {'dragon': dragon, 'giant': giant, 'wolf': wolf}


def dumb_question(real_boss):
    while True:
        final_ask = input(
            f"This is the determining time to face it\n Are you ready to face the most dangerous {real_boss['Name']} (type Yes)?")
        if final_ask.lower().strip() == "yes":
            break
        else:
            print("You cannot regret now, you must fight")


def three_boss_fight(character, boss_name):
    real_boss = boss()[boss_name].copy().copy()
    boss_list.call_monster(boss_name)
    boss_speech(boss_name)
    dumb_question(real_boss)
    # dragon: hp 20 , fight once_a_time, hit 2d4
    # giant: hp 15 , fight once, hit 1d12
    # wolf: hp 12, fight twice, hit 1d6
    while True:
        print(f"{character['Name']} draws his weapon and lunges at {real_boss['Name']}.")
        attack(character, real_boss)
        if real_boss['HP'][1] <= 0:
            print(f"you finally beat one of the dangerous boss {real_boss['Name']}\n ")
            print('now you can proceed')
            return True
        print(f"{real_boss['Name']} staggers and recovers its composure. It glares at you and Retaliates!")
        attack(real_boss, character, real_boss['times'], real_boss['roll'], real_boss['side'])
        if character['HP'][1] <= 0:
            print("you are dead from the boss fighting")
            return False


def boss_speech(choice):
    if choice == "dragon":
        print("""Congratulations on letting the evil dragon wake up, the world will fall into darkness, 
    his body, and the lethal flame spitting out of his mouth, approaching you step by step\n""")
        print("""The dragon has two dragon claws to give 2d4 attack points and 20 high HP points""")
    elif choice == "giant":
        print("""The giant approached you slowly with terrible brute force and giant body. 
    He seems to be telling you your insignificance, 
    full of murderousness, not disdain your challenge\n""")
        print("""The giant has giant fists to give 1d12 attack points and 15 semi-high HP points""")
    else:
        print("""The vicious wolf stares at you fiercely, he will not let go of the prey in front of him, 
    his fangs can easily tear the prey, he also runs towards you at a very fast speed, 
    you can only prepare your weapons to the enemy\n""")
        print("""The wolf has incredible speed 1d6 attack points and two times attack and 12 normal HP points""")


def main():
    doctest.testmod()
    GRID_EVENTS = {
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
    input("You have no idea what is going on and you wonder what this ‘arena’ is, so you ask the man for more details.")
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
        if int(intro_q1) == 1:
            print("    Death row inmate: 'Ajax the Giant is a Troll who stands as tall as three adult men.\n"
                  "                       He can single handedly crush you with a swing of his club.'\n")
        elif int(intro_q1) == 2:
            print("    Death row inmate: 'Fenrir the Great Wolf is a fierce beast whose speed is unrivaled in battle\n"
                  "                       in the time it takes you to land a hit he would've striked you twice.'\n")
        elif int(intro_q1) == 3:
            print("    Death row inmate: 'Cetus the Dragon has served in the king's bloodline for\n"
                  "                       thousands of years. His ferociousness is otherworldly and his thick hide\n"
                  "                       protects him from weapons that would pierce even walls'\n")
        elif int(intro_q1) == 4:
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
    #     'HP': [15, 1],
    #     'current_location': (3, 3)}
    print_character(my_char)

    input("You close your eyes to rest hoping that this is all a ridiculous nightmare.")

    print("You wake up to the sound of the screaming crowd as you stagger to your feet. You are in the arena\n"
          "and monsters surround you on all sides. You remember the What the old man said. . .\n"
          "To get out of here I must kill the three champions of this ARENA!\n")

    while my_char['HP'][1] > 0 and GRID_EVENTS['bosses']:
        # print(my_char['current_location'])
        grid_generator(my_char, GRID_EVENTS)
        quit_prompt = move_character(my_char)
        if quit_prompt:
            print("Thanks for playing our game! Please play again next time.")
            break
        else:
            boss_fight = boss_fight_checker(my_char, GRID_EVENTS)
            monster_battle = movement_checker(my_char)
            if boss_fight:
                if boss_fight == 'dragon':
                    three_boss_fight(my_char, boss_fight)
                elif boss_fight == 'giant':
                    three_boss_fight(my_char, boss_fight)
                else:
                    three_boss_fight(my_char, boss_fight)
            else:
                if monster_battle:
                    print("A monster catches up to you. Get ready for battle!")
                    normal_battle(my_char)


if __name__ == '__main__':
    main()
