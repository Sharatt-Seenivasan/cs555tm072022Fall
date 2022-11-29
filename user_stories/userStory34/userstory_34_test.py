from userstory_34 import *
from unittest.mock import patch

class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def test_large_age_difference(self, mock_print):
        large_age_difference(gedcom_file)
        mock_print.assert_called_with("US 34: Husband ID: Large age difference at marriage")


if __name__ == '__main__':
    unittest.main