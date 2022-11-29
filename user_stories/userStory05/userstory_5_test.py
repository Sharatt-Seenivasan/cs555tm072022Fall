from userStory41 import *
from unittest.mock import patch


class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def test_marriage_before_death1(self, mock_print):
        marriageBeforeDeath(gedcom_file)
        mock_print.assert_called_with("ERROR: US 06: Husband ID: Marriage before Death ")


if __name__ == '__main__':
    unittest.main