import unittest

def break_words(stuff):
    """This funciton will break up words for us."""
    words = stuff.split(' ')
    return words 


class MyTest(unittest.TestCase):

    def setUp(self):
        print 'In setUp()'
        self.fixture = break_words()

    def tearDown(self):
        print 'In tearDown()'
        del self.fixture

	#def testmethod(self):
	#	self.assertEqual(ex25.break_words(sentance), ['this', 'is', 'a', 'test', 'to', 'show', 'broken', 'words.'], 'test')

	def test_break(self):
		self.failUnlessEqual(['this', 'is', 'a', 'test', 'to', 'show', 'broken', 'words.'], self.fixture.break_words('This is a test.'))

if __name__ == '__main__':
    unittest.main()	