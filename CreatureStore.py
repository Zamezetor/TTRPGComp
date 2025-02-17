class charInit():
  def __init__(self, initiative, conditions, AC):
    self.initiative = initiative
    self.conditions = conditions
    self.armorClass = AC

  def getArmorClass(self):
    return self.armorClass
  
  def getConditions(self):
    return self.conditions
  
  def getInitative(self):
    return self.initiative