from rule import Rule
from hand import Hand
# Farkle Rules
# 
# Fives = 50
# ones = 100
# 
# 3 of a kind = face * 100 except ones 300
# 4 of a kind = 1000
# 5 of a kind = 2000
# 6 of a kind = 3000
# 1-6 straigt = 1,500
# Three pairs = 1,500
# Four of any number with a pair = 1500
# two triplets

class Single(Rule):
  def __init__(self, value: int, name: str, points: int, dice_min: int):
        self.__value: int = value
        self.__name: str = name
        self.__dice_minumum: int = dice_min
        self.__points: int = points

  def name(self) -> str:
      return self.__name

  def points(self) -> int:
      return self.__points

  def minumum(self) -> int:
      return self.__dice_minumum

  def check(self, hand: Hand) -> bool:
      if hand.count(self.__value) > 0:
        return True
      return False


class ThreeofaKind(Rule):
  def __init__(self, value: int, name: str, points: int):
        self.__value: int = value
        self.__name: str = name
        self.__dice_minumum: int = 3
        self.__points: int = points

  def name(self) -> str:
      return self.__name

  def points(self) -> int:
      return self.__points

  def minumum(self) -> int:
      return self.__dice_minumum

  def check(self, hand: Hand) -> bool:
      if hand.count(self.__value) >= self.__dice_minumum:
        return True
      return False


class XofaKind(Rule):
  def __init__(self, name: str, points: int, dice_minimum: int):
        self.__name: str = name
        self.__dice_minumum: int = dice_minimum
        self.__points: int = points

  def name(self) -> str:
      return self.__name

  def points(self) -> int:
      return self.__points

  def minumum(self) -> int:
      return self.__dice_minumum

  def check(self, hand: Hand) -> int:
      for i in range(6):
       if hand.count(i + 1) >= self.__dice_minumum:
        return True
      return False

# Singles
class Ones_Single(Single):

  def __init__(self):
    super().__init__(1, "Ones", 100, 1)

class Fives_Single(Single):

  def __init__(self):
    super().__init__(5, "Fives", 500, 1)


class Ones(ThreeofaKind):

  def __init__(self):
    super().__init__(1, "Three ones", 300)

class Twos(ThreeofaKind):

  def __init__(self):
    super().__init__(2, "Three twos", 200)

class Threes(ThreeofaKind):

  def __init__(self):
    super().__init__(3, "Three threes", 300) 

class Fours(ThreeofaKind):

  def __init__(self):
    super().__init__(4, "Three fours", 400)

class Fives(ThreeofaKind):

  def __init__(self):
    super().__init__(5, "Three fives", 500)

class Six(ThreeofaKind):

  def __init__(self):
    super().__init__(6, "Three fives", 600)

# 4,5,6 of a kind
class Four(XofaKind):

  def __init__(self):
    super().__init__("Four of a kind", 1000, 4)

class Five(XofaKind):

  def __init__(self):
    super().__init__("Five of a kind", 2000, 5)

class Six(XofaKind):

  def __init__(self):
    super().__init__("Six of a kind", 3000, 6)

class Three_Pairs(Rule):

  def name() -> int:
    return "Three pairs"

  def points(self) -> int:
    return 1500
  
  def minimum(self) -> int:
    return 6

  def check(self, hand: Hand) -> bool:
    counts = [hand.count(i + 1) for i in range(6)]
    # returns an array of counted numbers if 3 of them are = 2 then there are 3 pairs
    if(counts.count(2) == 3):
      return True
    return False

class Four_with_Pair(Rule):

  def name() -> str:
    return "Four of any number with a pair"

  def points(self) -> int:
    return 1500
  
  def minimum(self) -> int:
    return 6

  def check(self, hand) -> bool:
    counts = [hand.count(i + 1) for i in range(6)]
    # returns an array of counted numbers
    if(counts.count(2) == 1 and counts.count(4) == 1):
      return True
    return False

class Two_Triplets(Rule):

  def name() -> str:
    return "Two Triplets"

  def points(self) ->  int:
    return 2500
  
  def minimum(self) -> int:
    return 6

  def check(self, hand) -> bool:
    counts = [hand.count(i + 1) for i in range(6)]
    # returns an array of counted numbers 
    if(counts.count(3) == 2):
      return True
    return False

class Straight(Rule):

  def name() -> str:
    return "Two Triplets"

  def points(self) -> int:
    return 1500
  
  def minimum(self) -> int:
    return 6

  def check(self, hand) -> bool:
    counts = [hand.count(i + 1) for i in range(6)]
    # returns an array of counted numbers 
    if(counts.count(1) == 6):
      return True
    return False