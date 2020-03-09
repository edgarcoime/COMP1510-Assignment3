"""
Test the content of the boss dictionary
"""
from unittest import TestCase
import sud


class TestBoss(TestCase):
    def test_boss(self):
        expected = {'dragon': {'HP': [12, 12],
            'Name': 'Cetus the Dragon',
            'roll': 1,
            'side': 6,
            'times': 1},
 'giant': {'HP': [8, 8],
           'Name': 'Ajax the Giant',
           'roll': 1,
           'side': 8,
           'times': 1},
 'wolf': {'HP': [8, 8],
          'Name': 'Fenrir the Great Wolf',
          'roll': 1,
          'side': 4,
          'times': 2}}
        actual = sud.boss()
        self.assertEqual(expected, actual)