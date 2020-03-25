"""
Test three boss fight to get new update dictionary if player defeat one of bosses, or print died and return false if one of bosses defeat the player.
At last, print the congratulations if the player defeat all the bosses.
"""
from unittest import TestCase
import sud
from unittest.mock import patch
import io  # NEW


class TestThreeBossFight(TestCase):
    @patch('sud.roll_die', side_effect=[4, 4, 4, 4, 4])
    @patch('builtins.input', side_effect=["anything"])
    @patch('sud.boss',
           side_effect=[{'dragon': {'HP': [12, 12], 'Name': 'Cetus the Dragon', 'roll': 1, 'side': 6, 'times': 1}}])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three_boss_fight_defeat_dragon_by_attack_1d6_4_each_round_return_new_dictionary(self, mock_stdout, _, __,
                                                                                             ___):
        character = {"Name": "Player", "HP": [20, 20]}
        boss_name = "dragon"
        grid_events = {'bosses': {(1, 1): 'dragon', (5, 1): 'giant', (5, 5): 'wolf'}, 'events': None}
        expected = {'bosses': {(5, 1): 'giant', (5, 5): 'wolf'}, 'events': None}
        actual = sud.three_boss_fight(character, boss_name, grid_events)
        expected_print = """
                                        _.--.
                                     .' ,--.`.
                                   ,' ,'    `|
                                ,'  ,'      '
                              ,'   '
                            ,'    '
                         _,-    ,'
                      _,'       |                           ____,-------.
                   _,'           `.                   _,---'   ___,----. `.
                _,'             _,---.             ,-'      ,-'         `.|
             _,'            _,-'  _   `.        ,' __     ,'             |'
           ,'   .--.    _,-'__,--' `.   `.   ,'_,-'  `. ,'              ,'
        ,'  , '    `. ,'_,-'        `.    .,'-'-.      `.
      ,', '         ,','             `.          `-. `. `.
    ,','          ,''`)`.            ,`.         `.  `.`-.`.
   ,,'           ((  '   `.        ,'     _,-=-.  `\  `\ |`.
  ' (             ``       `.    ,'     ,'-,'  `.  `)  `)`  ))
 (   `                       ` .'     ,'-,'     |  ,;   ;  ''
  `                           `:     |---|      `.     ,'
                               :     |---|       '.    :
                               :     `.--`.       '.   :
                               `      `    `       ',`__) 

------------------------------------------------


 
You have woken the Dragon named Cetus. As it approaches you, you fight off the urge to run
away from the nightmarish beast in front of you clad with dark obsidian scales. As Cetus approaches
its mouth begins to froth with molten magma and his nostrils flair and emit steam. You take up arms
and ready yourself mentally and physically for battle that will unfold.

You have challenged Cetus the Dragon, one of the three champions in this arena.
His claws give it high attack of 2d4, and his draconic scales give him 12HP 
Player draws his weapon and lunges at Cetus the Dragon.
Player attacks Cetus the Dragon and deals 4 damage.
Leaving Cetus the Dragon with 8/12HP.

Cetus the Dragon staggers and recovers its composure. It glares at you and Retaliates!
Cetus the Dragon attacks Player and deals 4 damage.
Leaving Player with 16/20HP.

Player draws his weapon and lunges at Cetus the Dragon.
Player attacks Cetus the Dragon and deals 4 damage.
Leaving Cetus the Dragon with 4/12HP.

Cetus the Dragon staggers and recovers its composure. It glares at you and Retaliates!
Cetus the Dragon attacks Player and deals 4 damage.
Leaving Player with 12/20HP.

Player draws his weapon and lunges at Cetus the Dragon.
Player attacks Cetus the Dragon and deals 4 damage.
Leaving Cetus the Dragon with 0/12HP.

Congratulations! You have beaten Cetus the Dragon
You can now proceed to the other bosses in the arena.
"""
        self.assertEqual(expected, actual)
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('sud.roll_die', side_effect=[4, 4, 4])
    @patch('builtins.input', side_effect=[""])
    @patch('sud.boss',
           side_effect=[{'giant': {"Name": "Ajax the Giant", "HP": [8, 8], "side": 8, "roll": 1, "times": 1}}])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three_boss_fight_defeat_giant_by_attack_1d8_4_each_round_return_new_dictionary(self, mock_stdout, _, __,
                                                                                            ___):
        character = {"Name": "Player", "HP": [20, 20]}
        boss_name = "giant"
        grid_events = {'bosses': {(1, 1): 'dragon', (5, 1): 'giant', (5, 5): 'wolf'}, 'events': None}
        expected = {'bosses': {(1, 1): 'dragon', (5, 5): 'wolf'}, 'events': None}
        actual = sud.three_boss_fight(character, boss_name, grid_events)
        expected_print = """
    .#MMMMMMMMMb.
               d#+%XMMMMMMMMMMMM%b
            /%XXMMMMMMMMMMMMMMMMMMMb
     .-----.MMMMMMMMMMMMMMMMMMMMMMMM
    / -----/;+MMMMMMMMX+;= =+MMMMMMMM
   |  ----|;;MMMMMMMX-      ;M%%MMMMMX
   |   ---'/:+MMMMMM;       X%=  MMMMM
   |   |   /\+MMMMMM:       _._  %MMMM/
   |   :   | |MMMMM%/_-"-. :_ _:  XMMM%
   '.   '-/' |MMMMMM%'--'    '     |/|
    |      _/MMMMMX%     |         | |
    |     |'XMMMMM_/     |_        | /
    |     |  XMMM%%;:              |-
    |     |    %XMM+=   .---.      |
   .'     |     %%X%:,   ---    ,-'
   |      |         |'.      ._-':
   |      |        /   "-----"   |
  /       |    __./              |.
  |       |   /,.|                 -.
  |       |  /...|                   -..-.
 .'       | |....\                  /......
 |        |/|.....\                /......=-.
 |        | |......\.             /.....,-----.
.'          |.......'------------'......|      '.
|           |,.........................,|       |
|           |,......................... .       |
|           |......................... .        |
|          /...........................'       .'
 |        /...........................'        |
  '___   /.......................... |        .'
      '-'............................'        |
       |........................... |        .'
       |..........................,|         |
       |..........................-'        /
       |.........................'         /
       |....................... |         /
      /........................ |        |
     /.........................'        /
     |.......................,'        |
     ):......................|         |
     |,......................|        .+
     |.......................|       //|
     :---.__................/       |...\8
    /       "-_______-----""|       |... |
    .-                      |      .'... |
   .'.'-.                   |      |.......
  /......--.               .'     /........|
  '.........'-------------'|     |.........|
   |.....................,.'     |..........\8
   |....................,,|     .'............
   |....................,,|     |............|
   |.....................,|     |............|
   |...................../      |............|
------------------------------------------------

As you approach the Giant named Ajax his lips begin to curl upward as his monstrous body towers
before you. His club is the length and seems to weigh as much as he does; yet, he swings the club
effortlessly. You take a deep breath as you ready yourself for battle while Ajax laughs condescendingly.

You have challenged Ajax the Giant, one of the three champions in this arena.
His size gives him abnormal strength allowing him an attack of 1d8, his size gives him above average 8HP.
Player draws his weapon and lunges at Ajax the Giant.
Player attacks Ajax the Giant and deals 4 damage.
Leaving Ajax the Giant with 4/8HP.

Ajax the Giant staggers and recovers its composure. It glares at you and Retaliates!
Ajax the Giant attacks Player and deals 4 damage.
Leaving Player with 16/20HP.

Player draws his weapon and lunges at Ajax the Giant.
Player attacks Ajax the Giant and deals 4 damage.
Leaving Ajax the Giant with 0/8HP.

Congratulations! You have beaten Ajax the Giant
You can now proceed to the other bosses in the arena.
"""
        self.assertEqual(expected, actual)
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('sud.roll_die', side_effect=[4, 4, 4, 4, 4, 4])
    @patch('builtins.input', side_effect=[""])
    @patch('sud.boss',
           side_effect=[{'wolf': {"Name": "Fenrir the Great Wolf", "HP": [8, 8], "side": 4, "roll": 1, "times": 2}}])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three_boss_fight_defeat_wolf_by_attack_2d4_8_each_round_return_new_dictionary(self, mock_stdout, _, __,___):
        character = {"Name": "Player", "HP": [20, 20]}
        boss_name = "wolf"
        grid_events = {'bosses': {(1, 1): 'dragon', (5, 1): 'giant', (5, 5): 'wolf'}, 'events': None}
        expected = {'bosses': {(1, 1): 'dragon', (5, 1): 'giant'}, 'events': None}
        actual = sud.three_boss_fight(character, boss_name, grid_events)
        expected_print = """                         
                      ,oda8a888a888888bo,
                   ,od88888888aa888aa88a8bo,
                 ,da8888aaaa88a888aaaa8a8a88b,
                ,oa888aaaa8aa8888aaa8aa8a8a88o,
               ,88888aaaaaa8aa8888a8aa8aa888a88,
               8888a88aaaaaa8a88aa8888888a888888
               888aaaa88aa8aaaa8888; ;8888a88888
               Y888a888a888a8888;'   ;888888a88Y
                Y8a8aa8a888a88'      ,8aaa8888Y
                 Y8a8aa8aa8888;     ;8a8aaa88Y
                  `Y88aa8888;'      ;8aaa88Y'
          ,,;;;;;;;;'''''''         ;8888Y'
       ,,;                         ,888P
      ,;  ,;,                      ;""
     ;       ;          ,    ,    ,;
    ;  ;,    ;     ,;;;;;   ;,,,  ;
   ;  ; ;  ,' ;  ,;      ;  ;   ;  ;
   ; ;  ; ;  ;  '        ; ,'    ;  ;
   `;'  ; ;  '; ;,       ; ;      ; ',
        ;  ;,  ;,;       ;  ;,     ;;;
         ;,,;             ;,,;

------------------------------------------------

Fenrir stares at you as if he was looking at a rabbit that he could kill at any moment. From a
distance you can already tell that he was leagues above being just 'nimble'. He was fast and with
ferocity to match that speed as well. You prepare yourself sharpening your instincts as it approaches.

You have challenged Fenrir the Great Wolf, one of the three champions in this arena.
His speed allows him to attack twice with a roll of 1d4, compared to the others he is still fragileso he has average health of 6HP
Player draws his weapon and lunges at Fenrir the Great Wolf.
Player attacks Fenrir the Great Wolf and deals 4 damage.
Leaving Fenrir the Great Wolf with 4/8HP.

Fenrir the Great Wolf staggers and recovers its composure. It glares at you and Retaliates!
Fenrir the Great Wolf attacks with tremendous speed! Allowing it to strike Player 2 times.
Fenrir the Great Wolf rolls 4, 4 for a total of 8 damage. Leaving Player with 12/20HP.

Player draws his weapon and lunges at Fenrir the Great Wolf.
Player attacks Fenrir the Great Wolf and deals 4 damage.
Leaving Fenrir the Great Wolf with 0/8HP.

Congratulations! You have beaten Fenrir the Great Wolf
You can now proceed to the other bosses in the arena.
"""
        self.assertEqual(expected, actual)
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('sud.roll_die', side_effect=[1, 4, 4, 1, 4, 4, 1, 4, 4])
    @patch('builtins.input', side_effect=[""])
    @patch('sud.boss',
           side_effect=[{'wolf': {"Name": "Fenrir the Great Wolf", "HP": [8, 8], "side": 4, "roll": 1, "times": 2}}])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three_boss_fight_player_dead_by_wolf_attacked__2d4_8_each_round_only_fight_back_1_point_return_false_not_change_orignal_dictionary_print_finish_game(
            self, mock_stdout, _, __, ___):
        character = {"Name": "Player", "HP": [20, 20]}
        boss_name = "wolf"
        grid_events = {'bosses': {(1, 1): 'dragon', (5, 1): 'giant', (5, 5): 'wolf'}, 'events': None}
        actual = sud.three_boss_fight(character, boss_name, grid_events)
        expected_print = """                         
                      ,oda8a888a888888bo,
                   ,od88888888aa888aa88a8bo,
                 ,da8888aaaa88a888aaaa8a8a88b,
                ,oa888aaaa8aa8888aaa8aa8a8a88o,
               ,88888aaaaaa8aa8888a8aa8aa888a88,
               8888a88aaaaaa8a88aa8888888a888888
               888aaaa88aa8aaaa8888; ;8888a88888
               Y888a888a888a8888;'   ;888888a88Y
                Y8a8aa8a888a88'      ,8aaa8888Y
                 Y8a8aa8aa8888;     ;8a8aaa88Y
                  `Y88aa8888;'      ;8aaa88Y'
          ,,;;;;;;;;'''''''         ;8888Y'
       ,,;                         ,888P
      ,;  ,;,                      ;""
     ;       ;          ,    ,    ,;
    ;  ;,    ;     ,;;;;;   ;,,,  ;
   ;  ; ;  ,' ;  ,;      ;  ;   ;  ;
   ; ;  ; ;  ;  '        ; ,'    ;  ;
   `;'  ; ;  '; ;,       ; ;      ; ',
        ;  ;,  ;,;       ;  ;,     ;;;
         ;,,;             ;,,;

------------------------------------------------

Fenrir stares at you as if he was looking at a rabbit that he could kill at any moment. From a
distance you can already tell that he was leagues above being just 'nimble'. He was fast and with
ferocity to match that speed as well. You prepare yourself sharpening your instincts as it approaches.

You have challenged Fenrir the Great Wolf, one of the three champions in this arena.
His speed allows him to attack twice with a roll of 1d4, compared to the others he is still fragileso he has average health of 6HP
Player draws his weapon and lunges at Fenrir the Great Wolf.
Player attacks Fenrir the Great Wolf and deals 1 damage.
Leaving Fenrir the Great Wolf with 7/8HP.

Fenrir the Great Wolf staggers and recovers its composure. It glares at you and Retaliates!
Fenrir the Great Wolf attacks with tremendous speed! Allowing it to strike Player 2 times.
Fenrir the Great Wolf rolls 4, 4 for a total of 8 damage. Leaving Player with 12/20HP.

Player draws his weapon and lunges at Fenrir the Great Wolf.
Player attacks Fenrir the Great Wolf and deals 1 damage.
Leaving Fenrir the Great Wolf with 6/8HP.

Fenrir the Great Wolf staggers and recovers its composure. It glares at you and Retaliates!
Fenrir the Great Wolf attacks with tremendous speed! Allowing it to strike Player 2 times.
Fenrir the Great Wolf rolls 4, 4 for a total of 8 damage. Leaving Player with 4/20HP.

Player draws his weapon and lunges at Fenrir the Great Wolf.
Player attacks Fenrir the Great Wolf and deals 1 damage.
Leaving Fenrir the Great Wolf with 5/8HP.

Fenrir the Great Wolf staggers and recovers its composure. It glares at you and Retaliates!
Fenrir the Great Wolf attacks with tremendous speed! Allowing it to strike Player 2 times.
Fenrir the Great Wolf rolls 4, 4 for a total of 8 damage. Leaving Player with -4/20HP.

Your sight begins to blur as you feel you life fading away.
You have died. Please try again
"""
        self.assertFalse(actual)
        self.assertEqual(expected_print, mock_stdout.getvalue())

    @patch('sud.roll_die', side_effect=[4, 4, 4, 4, 4])
    @patch('builtins.input', side_effect=[""])
    @patch('sud.boss',
           side_effect=[{'dragon': {'HP': [12, 12], 'Name': 'Cetus the Dragon', 'roll': 1, 'side': 6, 'times': 1}}])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_three_boss_fight_defeat_three_bosses_and_last_one_is_dragon_return_a_empty_dictionary_in_the_value_of_bosses_print_finish_game(
            self, mock_stdout, _, __, ___):
        character = {"Name": "Player", "HP": [20, 20]}
        boss_name = "dragon"
        grid_events = {'bosses': {(1, 1): 'dragon'}, 'events': None}
        expected = {'bosses': {}, 'events': None}
        actual = sud.three_boss_fight(character, boss_name, grid_events)
        expected_print = """
                                        _.--.
                                     .' ,--.`.
                                   ,' ,'    `|
                                ,'  ,'      '
                              ,'   '
                            ,'    '
                         _,-    ,'
                      _,'       |                           ____,-------.
                   _,'           `.                   _,---'   ___,----. `.
                _,'             _,---.             ,-'      ,-'         `.|
             _,'            _,-'  _   `.        ,' __     ,'             |'
           ,'   .--.    _,-'__,--' `.   `.   ,'_,-'  `. ,'              ,'
        ,'  , '    `. ,'_,-'        `.    .,'-'-.      `.
      ,', '         ,','             `.          `-. `. `.
    ,','          ,''`)`.            ,`.         `.  `.`-.`.
   ,,'           ((  '   `.        ,'     _,-=-.  `\  `\ |`.
  ' (             ``       `.    ,'     ,'-,'  `.  `)  `)`  ))
 (   `                       ` .'     ,'-,'     |  ,;   ;  ''
  `                           `:     |---|      `.     ,'
                               :     |---|       '.    :
                               :     `.--`.       '.   :
                               `      `    `       ',`__) 

------------------------------------------------


 
You have woken the Dragon named Cetus. As it approaches you, you fight off the urge to run
away from the nightmarish beast in front of you clad with dark obsidian scales. As Cetus approaches
its mouth begins to froth with molten magma and his nostrils flair and emit steam. You take up arms
and ready yourself mentally and physically for battle that will unfold.

You have challenged Cetus the Dragon, one of the three champions in this arena.
His claws give it high attack of 2d4, and his draconic scales give him 12HP 
Player draws his weapon and lunges at Cetus the Dragon.
Player attacks Cetus the Dragon and deals 4 damage.
Leaving Cetus the Dragon with 8/12HP.

Cetus the Dragon staggers and recovers its composure. It glares at you and Retaliates!
Cetus the Dragon attacks Player and deals 4 damage.
Leaving Player with 16/20HP.

Player draws his weapon and lunges at Cetus the Dragon.
Player attacks Cetus the Dragon and deals 4 damage.
Leaving Cetus the Dragon with 4/12HP.

Cetus the Dragon staggers and recovers its composure. It glares at you and Retaliates!
Cetus the Dragon attacks Player and deals 4 damage.
Leaving Player with 12/20HP.

Player draws his weapon and lunges at Cetus the Dragon.
Player attacks Cetus the Dragon and deals 4 damage.
Leaving Cetus the Dragon with 0/12HP.

As you stand before the lifeless carcass of Cetus the Dragon the final champion.
You take a deep breath as you are overcome with the elation of escaping this nightmarish arena.
You breath in the last breath of air that you will take in this God forsaken place and look forward
to your new reborn life.
Thank you so much to play our game. Tha game producers are Edgar and Tommy
"""
        self.assertEqual(expected, actual)
        self.assertEqual(expected_print, mock_stdout.getvalue())
