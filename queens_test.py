import unittest

import queens

class Testing(unittest.TestCase):
	def test_string(self):
		
		d = [1, 1, 0, 0, 0, 0, 0, 0]
		self.assertFalse(queens.check_board(d, 2))

	def test_string1(self):
		
		d = [1, 2, 0, 0, 0, 0, 0, 0]
		self.assertFalse(queens.check_board(d, 2))
	
	def test_numberSolutins(self):
		
		self.assertEqual(queens.solve_board(8),92)
		
		self.assertEqual(queens.solve_board(9),352)
		
		self.assertEqual(queens.solve_board(10),724)

if __name__ == '__main__':
	unittest.main()
	