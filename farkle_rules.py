from rule import Rule
from hand import Hand
# Farkle Rules
# 
# Fives = 50
# ones = 100
#
# 3 of a kind = face * 100
# 40 of a kind = 1000
# 5 of a kind = 2000
# 6 of a kind = 3000
# 1-6 straigt = 1,500
# Three pairs = 1,500
# Four of any number with a pair = 1500
# two triplets

class Single(Rule):
  def __init__(self, value: int, name: str, dice_min: int):
        self.__value = value
        self.__name = name
        self.__dice_minumum = dice_min

  def name(self):
      return self.__name

  def points(self, hand: Hand):
      return hand.count(self.__value) * self.__value

  def minumum(self):
      return self.__dice_minumum

class Ones(Single):

  def __init__(self):
    super().__init__(100, "Ones", 1)

class Fives(Single):

  def __init__(self):
    super().__init__(500, "Ones", 1)