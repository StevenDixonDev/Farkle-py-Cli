import unittest
from dice import Die

class dietests(unittest.TestCase):
#test has to start with test_
    def test_create(self):
        dice = Die(6)
        self.assertTrue(dice.get_face() > 0)

    def test_set_face(self):
        die = Die(6)
        die.set_face(4)
        self.assertEquals(die.get_face(), 4)

if __name__ == '__main__':
    unittest.main()