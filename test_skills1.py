import unittest

from skills1 import *

class TestSkills(unittest.TestCase):

	def setUp(self):
		self.words = ["hello", "my", "name", "is", "Michaela", "and", "I", "am", "a", "lady"]
		self.numbers = [1, 2, 7, 12, 15, -2, 3, -17, 100, -2]


	def test_1_A_all_odd(self):
		self.assertEqual(all_odd(self.numbers), [1, 7, 15, 3, -17])

	def test_1_B_all_even(self):
		self.assertEqual(all_even(self.numbers), [2, 12, -2, 100, -2])

	def test_1_C_long_words(self):
		self.assertEqual(long_words(self.words), ["hello", "name", "Michaela", "lady"])

	def test_1_D_smallest(self):
		self.assertEqual(smallest(self.numbers), -17)

	def test_1_E_largest(self):
		self.assertEqual(largest(self.numbers), 100)

	def test_1_F_halvesies(self):
		self.assertEqual(halvesies(self.numbers), [.5, 1, 3.5, 6, 7.5, -1, 1.5, -8.5, 50, -1])

	def test_1_G_word_lengths(self):
		self.assertEqual(word_lengths(self.words), [5, 2, 4, 2, 8, 3, 1, 2, 1, 4])

	def test_1_H_sum_numbers(self):
		self.assertEqual(sum_numbers(self.numbers), 119)

	def test_1_I_mult_numbers(self):
		self.assertEqual(mult_numbers(self.numbers), -51408000)

	def test_1_J_join_strings(self):
		self.assertEqual(join_strings(self.words), "hellomynameisMichaelaandIamalady")

	def test_1_K_average(self):
		self.assertEqual(average(self.numbers), 11.9)

	def test_1_L_custom_map(self):
		self.assertEqual(custom_map(lambda x: x * 2, self.numbers), [2, 4, 14, 24, 30, -4, 6, -34, 200, -4])

	def test_1_M_custom_filter(self):
		self.assertEqual(custom_filter(lambda x: x % 2 == 0, self.numbers), [2, 12, -2, 100, -2])

	def test_1_N_custom_reduce(self):
		self.assertEqual(custom_reduce(lambda x, y: x + y, self.numbers), 119)

if __name__ == '__main__':
	unittest.main()

