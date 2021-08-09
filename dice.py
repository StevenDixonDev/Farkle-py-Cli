import random


class Die:
    def __init__(self, sides):
      self.__sides = sides
      self.__face = 0
      self.__can_roll = True
      self.roll()
      pass

    def roll(self):
      if self.__can_roll == True:
        self.__face = random.randint(1, self.__sides)
      return self.__face

    def get_face(self):
      return self.__face

    def set_face(self, value):
      self.__face = value

    def set_can_roll(self, value):
      self.__can_roll = value
    
    def get_can_roll(self):
      return self.__can_roll

    def __str__(self):
      return '{self.currentValue}'.format(self)