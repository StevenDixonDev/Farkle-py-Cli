from dice import Die

class Hand:
  def __init__(self, hand_size = 5):
    self.__hand_size = hand_size
    self.__dice = []
    self.create_hand()

  def create_hand(self):
      for _ in range(self.__hand_size):
        self.__dice.append(Die(6))

  def get_hand(self):
      return [die.get_face() for die in self.__hand]

  def roll_hand(self):
     for x in range(self.__hand_size):
      # x is an int representing the current index in the size of the hand
      self.__dice[x].roll()

  def roll_selected_dice(self, selected_dice):
    for x in selected_dice:
      selected_dice.roll()

  def __str__(self):
    return '/n'.join(["die {idx} has value {die}".format(idx, die) for idx, die in self.__hand])
