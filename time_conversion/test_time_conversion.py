import unittest

from time_conversion import solution

class TestTimeConversion(unittest.TestCase):
    def test_01_pm(self):
        self.assertEqual(solution("07:05:45PM"), "19:05:45")

    def test_01_am(self):
        self.assertEqual(solution("07:05:45AM"), "07:05:45")

    def test_caso_especial_am(self):
        self.assertEqual(solution("12:05:39AM"), "00:05:39")

    def test_caso_especial_pm(self):
        self.assertEqual(solution("12:45:54PM"), "12:45:54")

if __name__ == '__main__': 
    unittest.main()