import unittest
 
 
 
class DummyText(unittest.TestCase): 
 
    def setUp(self):
        self.pi = 3.14
        self.information = "I´m setting up stuff first, after this the tests below will run"
 
    def test_nothing(self):
        self.assertTrue(False)
  
    def tearDown(self):
        self.information = "I will destroy the stuff setted up (e.g. widgets, windows)"