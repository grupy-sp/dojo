import unittest

class ExemploTest(unittest.TestCase):
    def testPassa(self):
        self.assertTrue(True)

    def testFalha(self):
        self.assertFalse(True)