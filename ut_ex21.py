from nose.tools import *
import ex21
import unittest
import sys

class MyTest(unittest.TestCase):
	def testmethod(self):
		self.assertEqual(ex21.add(1, 2), 3, 'Add Test')

if __name__ == '__main__':
    unittest.main()		