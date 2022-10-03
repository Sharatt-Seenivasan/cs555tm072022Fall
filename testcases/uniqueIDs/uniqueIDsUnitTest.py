import os
import unittest
from uniqueIDs import unique_ids

class TestStringMethods(unittest.TestCase):

    filename_dir = os.path.dirname(os.path.abspath(__file__))

    def test_file_1(self):
        self.assertEqual()

    filename1 = filename_dir + '/uniqueIDsTestData1.xlsx'
    filename2 = filename_dir + '/uniqueIDsTestData2.xlsx'
    filename3 = filename_dir + '/uniqueIDsTestData3.xlsx'
    filename4 = filename_dir + '/uniqueIDsTestData4.xlsx'
    filename5 = filename_dir + '/uniqueIDsTestData5.xlsx'

    unique_ids(filename1)
    unique_ids(filename2)
    unique_ids(filename3)
    unique_ids(filename4)
    unique_ids(filename5)

if __name__ == '__main__':
    unittest.main()