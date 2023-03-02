import os
import unittest
from python_homework import Main


class TestReadFile(unittest.TestCase):
    TESTDATA_FILENAME = os.path.abspath(os.path.dirname(__file__)) + "/10000_Sales_Records.csv"

    def setUp(self):
        self.test_file = open(self.TESTDATA_FILENAME, "r")

    def test_invalid_file_format(self):
        file_name = "myfile.png"
        with self.assertRaises(Exception) as e:
            Main.read_file(file_name)
        self.assertEqual(str(e.exception), "File Format is not correct!")

    def test_valid_test_case(self):
        file = Main.read_file(self.TESTDATA_FILENAME)
        self.assertEqual(type(file), type(self.test_file))


if __name__ == '__main__':
    unittest.main()
