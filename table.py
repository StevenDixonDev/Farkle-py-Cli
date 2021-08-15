from hand import Hand
from rule import Rule

# keeps track of rules and current points
class ScoreTable:
  def __init__(self):
    self.__rules: list = []
    self.__points_per_rule: list = []
   
  def add_rule(self, rule) -> None:
    # add a rule to rule list
    self.__rules.extend(rule)

    # set scores to length of rule list
    self.__points_per_rule = [0] * len(self.__rules)

  def get_total_points(self) -> int:
    return  sum(self.__points_per_rule)

  def assign_points(self, hand: Hand) -> None:
    # todo add in calculations after defining rules
    pass



