import unittest
from app import addition
class TestAdditionMethod(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(5, addition(2,3))
    def test_is_upper(self):
        self.assertTrue("UPPER".isupper())


if __name__ == '__main__':
    unittest.main()