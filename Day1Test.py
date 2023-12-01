import unittest
from Day1 import main_2


class TestRun(unittest.TestCase):
    def test_run(self):
        self.assertEqual(45000, main_2())


if __name__ == '__main__':
    unittest.main()
