import unittest
from Day1 import main


class TestRun(unittest.TestCase):
    def test_run(self):
        self.assertEqual(74394, main())


if __name__ == '__main__':
    unittest.main()
