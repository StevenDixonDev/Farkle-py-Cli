from hand import Hand

# keeps track of rules and current points
class ScoreTable:
  def __init__(self):
    self.__rules = []
    self.__points_per_rule = []
   
  def add_rule(self, rule):
    # add a rule to rule list
    self.__rules.extend(rule)

    # set scores to length of rule list
    self.__points_per_rule = [0] * len(self.__rules)

  def get_total_points(self):
    return  sum(self.__points_per_rule)

  def assign_points(self, hand):
    # todo add in calculations after defining rules
    pass



