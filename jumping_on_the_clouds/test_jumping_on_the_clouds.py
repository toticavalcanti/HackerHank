import unittest

from jumping_on_the_clouds import jumping

class TestJumpingClouds(unittest.TestCase):
	def test_0010(self):
		self.assertEqual(jumpingOnClouds(['0010']), 96)

	def test_00100110(self): #8  2
		self.assertEqual(jumpingOnClouds(['00100110']), 92)

	def test_011010110110000011111010	(self):#24  3
		self.assertEqual(jumpingOnClouds(['011010110110000011111010']), 86)

	def test_1101010101011011111(self):#19  19
		self.assertEqual(jumpingOnClouds(['1101010101011011111']), 97)

	def test_1111111111111111(self): #16   1
		self.assertEqual(jumpingOnClouds(['1111111111111111']), 52)

	def test_0010111111100011(self): #16   2
		self.assertEqual(jumpingOnClouds(['0010111111100011']), 80)

	def test_1110110000(self): #2    1
		self.assertEqual(jumpingOnClouds(['01']), 96)

if __name__ == '__main__': 
    unittest.main()

