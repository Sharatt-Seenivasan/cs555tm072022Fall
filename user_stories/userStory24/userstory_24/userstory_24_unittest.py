import os
import sys
import unittest
from unittest.mock import patch
from userstory_24 import *

sys.path.append('')
from gedcom_helper import file_parser, output_data

class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def test_file_1(self, mock_print):
        filename1 = os.path.dirname(os.path.abspath(__file__)) + '/userstory_24_testdata1.ged'
        individuals, families = file_parser(filename1)
        output = output_data(individuals, families, filename1)
        unique_families(families)
        mock_print.assert_called_with('ERROR: FAMILY: US24: F2 is not a unique ID with a unique spouse.')

if __name__ == '__main__':
    unittest.main()