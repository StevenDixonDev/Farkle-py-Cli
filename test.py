import unittest
from dice import Die
from hand import Hand
from rule import Rule
from farkle_rules import Rule

# Unit testing with unit test library
# assertEqual a==b
# assertTrue/False bool is true/false
# assertIs a is b
# assertIsNone is None
# assertIn  a in b *t
# assertIsInstance a is instance of b *best used to test typings

class DieTests(unittest.TestCase):
#test has to start with test_
    def test_create(self):
        dice = Die(6)
        # verify dice is instanced properly
        self.assertIsInstance(dice, Die)
        # verify dice face is always greater than zero
        self.assertTrue(dice.get_face() > 0)

    def test_set_get_face(self):
        die = Die(6)
        die.set_face(4)
        self.assertEqual(die.get_face(), 4)

    def test_roll(self):
        dice = Die(6)

        for x in range(1000):
            dice.roll()
            self.assertGreater(dice.get_face(), 0)
            self.assertLessEqual(dice.get_face(), 6)

    def test_can_roll(self):
        dice = Die(6)

        # set dice to not roll
        dice.set_can_roll(False)
        current_face = dice.get_face()
        # test rolled face vs recorded face
        for x in range(1000):
            dice.roll()
            self.assertEqual(current_face, dice.get_face())


class HandTests(unittest.TestCase):

    def test_create_default(self):
        hand = Hand()
        # verify hand instanced correctly
        self.assertIsInstance(hand, Hand)
        # verify hand size default works properly
        self.assertEqual(len(hand.get_hand()), 6)
        
    def test_create_hand(self):
        hand_sizes = [1, 4, 5, 6, 20]

        for x in hand_sizes:
            hand = Hand(x)
            # verify hand instanced correctly
            self.assertIsInstance(hand, Hand)
            # verify hand size default works properly
            self.assertEqual(len(hand.get_hand()), x)

    def test_get_hand(self):
        hand = Hand()
        for x in hand.get_hand():
            # check if face is number
            self.assertIsInstance(x, int)

    def test_roll_hand(self):
        pass

    def test_selected_roll(self):
        pass

if __name__ == '__main__':
    unittest.main()


