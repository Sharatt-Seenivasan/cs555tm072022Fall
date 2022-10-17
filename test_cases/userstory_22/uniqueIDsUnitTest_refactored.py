import os
import unittest
from unittest.mock import patch
from userstory_22_refactored import *
from helper_functions import file_parser

class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def test_file_1(self, mock_print):
        filename1 = os.path.dirname(os.path.abspath(__file__)) + '/uniqueIDsTestData1.ged'
        individuals, families = file_parser(filename1)
        unique_ids(individuals, families)
        mock_print.assert_called_with('ERROR (US22): ID I3 is not a unique ID.')

    @patch('builtins.print')
    def test_file_2(self, mock_print):
        filename2 = os.path.dirname(os.path.abspath(__file__)) + '/uniqueIDsTestData2.ged'
        individuals, families = file_parser(filename2)
        unique_ids(individuals, families)
        mock_print.assert_called_with('ERROR (US22): ID F6 is not a unique ID.')

    @patch('builtins.print')
    def test_file_3(self, mock_print):
        filename3 = os.path.dirname(os.path.abspath(__file__)) + '/uniqueIDsTestData3.ged'
        individuals, families = file_parser(filename3)
        unique_ids(individuals, families)
        mock_print.assert_called_with('ERROR (US22): ID F4 is not a unique ID.\nERROR (US22): ID F5 is not a unique ID.')

    @patch('builtins.print')
    def test_file_4(self, mock_print):
        filename4 = os.path.dirname(os.path.abspath(__file__)) + '/uniqueIDsTestData4.ged'
        individuals, families = file_parser(filename4)
        unique_ids(individuals, families)
        mock_print.assert_called_with('ERROR (US22): ID I7 is not a unique ID.\nERROR (US22): ID I8 is not a unique ID.')

    @patch('builtins.print')
    def test_file_5(self, mock_print):
        filename5 = os.path.dirname(os.path.abspath(__file__)) + '/uniqueIDsTestData5.ged'
        individuals, families = file_parser(filename5)
        unique_ids(individuals, families)
        mock_print.assert_called_with('File has all unique IDs.')

if __name__ == '__main__':
    unittest.main()