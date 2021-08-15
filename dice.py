import random


class Die:
    def __init__(self, sides: int):
      self.__sides: int = sides
      self.__face: int = 0
      self.__can_roll: bool = True
      self.roll()
      pass

    def roll(self) -> int:
      if self.__can_roll == True:
        self.__face = random.randint(1, self.__sides)
      return self.__face

    def get_face(self) -> int:
      return self.__face

    def set_face(self, value) -> None:
      self.__face = value

    def set_can_roll(self, value) -> None:
      self.__can_roll = value
    
    def get_can_roll(self) ->  bool:
      return self.__can_roll

    def __str__(self) -> str:
      return '{self.currentValue}'.format(self)