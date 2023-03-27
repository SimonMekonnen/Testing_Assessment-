import unittest
from string_functions import *

# Define a test case for the to_upper() function
class TestToUpper(unittest.TestCase):
    def test_to_upper(self):
        # Test the function with different inputs and expected outputs using the assertEqual() method
        self.assertEqual(to_upper("hello"), "HELLO")
        self.assertEqual(to_upper("WORLD"), "WORLD")
        self.assertEqual(to_upper("123"), "123")
        self.assertEqual(to_upper(""), "")

# Define a test case for the to_lower() function
class TestToLower(unittest.TestCase):
    def test_to_lower(self):
        # Test the function with different inputs and expected outputs using the assertEqual() method
        self.assertEqual(to_lower("HELLO"), "hello")
        self.assertEqual(to_lower("world"), "world")
        self.assertEqual(to_lower("123"), "123")
        self.assertEqual(to_lower(""), "")

# Define a test case for the capitalize() function
class TestCapitalize(unittest.TestCase):
    def test_capitalize(self):
        # Test the function with different inputs and expected outputs using the assertEqual() method
        self.assertEqual(capitalize("hello"), "Hello")
        self.assertEqual(capitalize("WORLD"), "World")
        self.assertEqual(capitalize("123"), "123")
        self.assertEqual(capitalize(""), "")

# Run the tests using the unittest.main() function
if __name__ == '__main__':
    unittest.main()
