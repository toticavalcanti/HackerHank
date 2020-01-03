import unittest

from find_digits import solution

class TestFindDigits(unittest.TestCase):
    def test_111(self):
        self.assertEqual(solution(111), 3)

    def test_1012(self):
        self.assertEqual(solution(1012), 3)

    def test_12(self):
        self.assertEqual(solution(12), 2)

if __name__ == '__main__':
    unittest.main()