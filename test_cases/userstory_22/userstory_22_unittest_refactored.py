import os
import unittest
from unittest.mock import patch
from userstory_22_refactored import *
from testing.helper_functions import file_parser

class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def test_file_1(self, mock_print):
        filename1 = os.path.dirname(os.path.abspath(__file__)) + '/testing/userstory_22_testdata1.ged'
        individuals, families = file_parser(filename1)
        unique_ids(individuals, families)
        mock_print.assert_called_with('ERROR: INDIVIDUAL: US22: I3 is not a unique Individual ID.')

    @patch('builtins.print')
    def test_file_2(self, mock_print):
        filename2 = os.path.dirname(os.path.abspath(__file__)) + '/testing/userstory_22_testdata2.ged'
        individuals, families = file_parser(filename2)
        unique_ids(individuals, families)
        mock_print.assert_called_with('ERROR: FAMILY: US22: F6 is not a unique Family ID.')

    @patch('builtins.print')
    def test_file_3(self, mock_print):
        filename3 = os.path.dirname(os.path.abspath(__file__)) + '/testing/userstory_22_testdata3.ged'
        individuals, families = file_parser(filename3)
        unique_ids(individuals, families)
        mock_print.assert_called_with('ERROR: FAMILY: US22: F4 is not a unique Family ID.\nERROR: FAMILY: US22: F5 is not a unique Family ID.')

    @patch('builtins.print')
    def test_file_4(self, mock_print):
        filename4 = os.path.dirname(os.path.abspath(__file__)) + '/testing/userstory_22_testdata4.ged'
        individuals, families = file_parser(filename4)
        unique_ids(individuals, families)
        mock_print.assert_called_with('ERROR: INDIVIDUAL: US22: I7 is not a unique Individual ID.\nERROR: INDIVIDUAL: US22: I8 is not a unique Individual ID.')

    @patch('builtins.print')
    def test_file_5(self, mock_print):
        filename5 = os.path.dirname(os.path.abspath(__file__)) + '/testing/userstory_22_testdata5.ged'
        individuals, families = file_parser(filename5)
        unique_ids(individuals, families)
        mock_print.assert_called_with('File has all unique IDs.')

if __name__ == '__main__':
    unittest.main()