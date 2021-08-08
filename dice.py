import random


class Die:
    def __init__(self, sides):
      self.__sides = sides
      self.__face = 0
      self.roll()
      pass

    def roll(self):
      self.__face = random.randint(1, self.__sides)
      return self.__face

    def get_face(self):
      return self.__face

    def set_face(self, value):
      self.__face = value

    
    def __str__(self):
      return '{self.currentValue}'.format(self)