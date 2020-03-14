"""
test print character function to make sure it displays the character information page properly and is well formatted.
"""

from unittest import TestCase

import unittest.mock
import io
import sud


class TestPrintCharacter(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character(self, mock_stdout):
        character_dictionary = {
            'Name': 'Edgar',
            'Class': 'bard',
            'Race': 'dwarf',
            'HP': [20, 20],
            'current_location': (3, 3)
        }

        expected_print = "These are the characteristics that you remember.\n" \
                         "Name: Edgar\n" \
                         "Hit-Points: 20/20\n" \
                         "Class: Bard\n" \
                         "Race: Dwarf\n\n\n"
        sud.print_character(character_dictionary)
        self.assertEqual(mock_stdout.getvalue(), expected_print, "Passed dictionary is properly formatted and valid.")
