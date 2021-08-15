from abc import ABC, abstractmethod, abstractproperty
from hand import Hand

class Rule(ABC):

  @abstractmethod
  def name(self):
    pass

  @abstractmethod
  def points(self, hand: Hand):
    pass

  @abstractmethod
  def minumum(self):
    pass

  @abstractmethod
  def check(self, hand: Hand):
    pass
