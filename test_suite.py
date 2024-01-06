import unittest

from my_function import add_numbers

class TestFunction(unittest.TestCase):

    def test_addition(self):
        result = add_numbers(3,5)
        self.assertEqual(result, 8)
        
if __name__ == '__main__':
    unittest.main()