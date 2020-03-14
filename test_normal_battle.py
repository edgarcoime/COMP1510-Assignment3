"""
Test choosing a random monster name in a list and type fight or run to implement the functions to show the combat or
escape. In the fighting part, show two types of results: defeat monster or monster defeat player. Finally, retype if
the player didn't type fight or run correctly.
"""
from unittest import TestCase
import sud
from unittest.mock import patch
import io  # NEW


class TestNormalBattle(TestCase):
    @patch('sud.roll_die', side_effect=[4, 3, 2])
    @patch('random.choice', side_effect=['Gael (Katakan)'])
    @patch('builtins.input', side_effect=["fight"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_normal_battle_choose_fight_attack_defeat_monster_by_attack_4_2_total_6(self, mock_stdout, _, __, ___):
        character = {"Name": "Player", "HP": [20, 20]}
        sud.normal_battle(character)
        expected_print = """You meet a monster named Gael (Katakan)
Player draws his weapon and lunges at the beast.
Player attacks Gael (Katakan) and deals 4 damage.
Leaving Gael (Katakan) with 1/5HP.

Gael (Katakan) staggers and recovers its composure. It glares at you and Retaliates!
Gael (Katakan) attacks Player and deals 3 damage.
Leaving Player with 17/20HP.

Player draws his weapon and lunges at the beast.
Player attacks Gael (Katakan) and deals 2 damage.
Leaving Gael (Katakan) with -1/5HP.

You have successfully killed the monster Gael (Katakan)!

"""
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('sud.roll_die', side_effect=[1, 6, 1, 6, 1, 6,1,6])
    @patch('random.choice', side_effect=['White Lady (Noonwraith)'])
    @patch('builtins.input', side_effect=["fight"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_normal_battle__choose_fight_attack_player_dead_attack_1_harm_6_each_time(self, mock_stdout, _, __, ___):
        character = {"Name": "Player", "HP": [20, 20]}
        sud.normal_battle(character)
        expected_print = """You meet a monster named White Lady (Noonwraith)
Player draws his weapon and lunges at the beast.
Player attacks White Lady (Noonwraith) and deals 1 damage.
Leaving White Lady (Noonwraith) with 4/5HP.

White Lady (Noonwraith) staggers and recovers its composure. It glares at you and Retaliates!
White Lady (Noonwraith) attacks Player and deals 6 damage.
Leaving Player with 14/20HP.

Player draws his weapon and lunges at the beast.
Player attacks White Lady (Noonwraith) and deals 1 damage.
Leaving White Lady (Noonwraith) with 3/5HP.

White Lady (Noonwraith) staggers and recovers its composure. It glares at you and Retaliates!
White Lady (Noonwraith) attacks Player and deals 6 damage.
Leaving Player with 8/20HP.

Player draws his weapon and lunges at the beast.
Player attacks White Lady (Noonwraith) and deals 1 damage.
Leaving White Lady (Noonwraith) with 2/5HP.

White Lady (Noonwraith) staggers and recovers its composure. It glares at you and Retaliates!
White Lady (Noonwraith) attacks Player and deals 6 damage.
Leaving Player with 2/20HP.

Player draws his weapon and lunges at the beast.
Player attacks White Lady (Noonwraith) and deals 1 damage.
Leaving White Lady (Noonwraith) with 1/5HP.

White Lady (Noonwraith) staggers and recovers its composure. It glares at you and Retaliates!
White Lady (Noonwraith) attacks Player and deals 6 damage.
Leaving Player with -4/20HP.

You are dealt a fatal wound and everything turns black. All you hear are the monsters gathering 
around your body and the sound of your flesh being eaten.
"""
        self.assertEqual(expected_print, mock_stdout.getvalue())


    @patch('sud.roll_die', side_effect=[1, 4])
    @patch('random.choice', side_effect=['Morvudd(Fiend)'])
    @patch('builtins.input', side_effect=["run"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_normal_battle_choose_run_but_get_the_chance_being_hurt_by_4_points(self, mock_stdout, _, __, ___):
        character = {"Name": "Player", "HP": [20, 20]}
        sud.normal_battle(character)
        expected_print = """You meet a monster named Morvudd(Fiend)
You have a 10% chance of being backstabbed.
While retreating you are attacked from behind!
You are hit with 4 damage, leaving you with 16/20HP.

"""
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('sud.roll_die', side_effect=[3])
    @patch('random.choice', side_effect=['Morvudd(Fiend)'])
    @patch('builtins.input', side_effect=["run"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_normal_battle_choose_run_and_successfully_escape(self, mock_stdout, _, __, ___):
        character = {"Name": "Player", "HP": [20, 20]}
        sud.normal_battle(character)
        expected_print = """You meet a monster named Morvudd(Fiend)
You have a 10% chance of being backstabbed.
You successfully escape!

"""
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('sud.roll_die', side_effect=[6])
    @patch('random.choice', side_effect=['Morvudd(Fiend)'])
    @patch('builtins.input', side_effect=["rn", "run"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_normal_battle_type_wrong_word_and_type_again_choose_run_and_successfully_escape(self, mock_stdout, _, __, ___):
        character = {"Name": "Player", "HP": [20, 20]}
        sud.normal_battle(character)
        expected_print = """You meet a monster named Morvudd(Fiend)
That is not a valid input please type 'run' or 'fight'
You have a 10% chance of being backstabbed.
You successfully escape!

"""
        self.assertEqual(expected_print, mock_stdout.getvalue())