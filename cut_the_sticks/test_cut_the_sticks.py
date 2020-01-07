import unittest

from cut_the_sticks import cutTheSticks


class TestCutTheSticks(unittest.TestCase):
    def test_1(self):
        self.assertEqual(cutTheStickscutTheSticks([1]), [1])
    def test_544228(self):
        self.assertEqual(cutTheSticks([5, 4, 4, 2, 2, 8]), [6, 4, 2, 1])


if __name__ == '__main__':
    unittest.main()