import unittest
from app import addition
class TestAdditionMethod(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(5, addition(2,3))


if __name__ == '__main__':
    unittest.main()