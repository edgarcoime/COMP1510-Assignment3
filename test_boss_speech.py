"""
Test different choices having three types of background boss stories
"""
from unittest import TestCase
import sud
import unittest.mock  # NEW
import io  # NEW

class TestBossSpeech(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_speech_dragon(self, mock_stdout):
        expected = """You have woken the Dragon named Cetus. As it approaches you, you fight off the urge to run
away from the nightmarish beast in front of you clad with dark obsidian scales. As Cetus approaches
its mouth begins to froth with molten magma and his nostrils flair and emit steam. You take up arms
and ready yourself mentally and physically for battle that will unfold.

You have challenged Cetus the Dragon, one of the three champions in this arena.
His claws give it high attack of 2d4, and his draconic scales give him 12HP 
"""
        sud.boss_speech('dragon')
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_speech_giant(self, mock_stdout):
        expected = """As you approach the Giant named Ajax his lips begin to curl upward as his monstrous body towers
before you. His club is the length and seems to weigh as much as he does; yet, he swings the club
effortlessly. You take a deep breath as you ready yourself for battle while Ajax laughs condescendingly.

You have challenged Ajax the Giant, one of the three champions in this arena.
His size gives him abnormal strength allowing him an attack of 1d8, his size gives him above average 8HP.
"""
        sud.boss_speech('giant')
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_speech_wolf(self, mock_stdout):
        expected = """Fenrir stares at you as if he was looking at a rabbit that he could kill at any moment. From a
distance you can already tell that he was leagues above being just 'nimble'. He was fast and with
ferocity to match that speed as well. You prepare yourself sharpening your instincts as it approaches.

You have challenged Fenrir the Great Wolf, one of the three champions in this arena.
His speed allows him to attack twice with a roll of 1d4, compared to the others he is still fragileso he has average health of 6HP
"""
        sud.boss_speech('wolf')
        self.assertEqual(expected, mock_stdout.getvalue())
