import unittest
from fibo import *


class FibonacciTest(unittest.TestCase):
	def test_fibonacci_upto_1(self):
        	result = fib(1)  # Function doesn't exist yet
        	self.assertEqual(result, [0])
    
	def test_fibonacci_upto_2(self):
        	result = fib(2)
        	self.assertEqual(result, [0, 1])
    
	def test_fibonacci_upto_3(self):
        	result = fib(3)
        	self.assertEqual(result, [0, 1, 1])

	def test_fibonacci_upto_4(self):
		result = fib(4)
		self.assertEqual(result, [0, 1, 1, 2])

	def test_fibonacci_0(self):
		result = fib(0)
		self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()

