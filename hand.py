from typing import List
from dice import Die

class Hand:
  def __init__(self, hand_size: int = 6):
    self.__hand_size: int = hand_size
    self.__dice: list = []
    self.create_hand()

  def create_hand(self) -> None:
      for _ in range(self.__hand_size):
        self.__dice.append(Die(6))

  def get_hand(self) -> list:
      return [die.get_face() for die in self.__dice]

  def roll_hand(self) -> None:
     for x in range(self.__hand_size):
      # x is an int representing the current index in the size of the hand
      self.__dice[x].roll()

  def roll_selected_dice(self, selected_dice) -> None:
    for x in selected_dice:
      self.__dice[x].roll()


  def __str__(self) -> str:
    return '/n'.join(["die {idx} has value {die}".format(idx, die) for idx, die in self.__hand])
