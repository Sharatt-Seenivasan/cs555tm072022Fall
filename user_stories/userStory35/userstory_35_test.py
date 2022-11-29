from userstory_35 import *
from unittest.mock import patch

class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def list_recent_births_test1(self, mock_print):
        listRecentBirths(gedcom_file)
        mock_print.assert_called_with("US 35: Husband ID: Recently was born ")


if __name__ == '__main__':
    unittest.main