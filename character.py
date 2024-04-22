class Character:
  def __init__(self, name, max_health):
    self.name = name
    self.max_health = max_health
    self.health = self.max_health
    self.level = 1
    self.xp = 0
    self.knocked_out = False

  def knock_out(self):
    self.knocked_out = True
    print(f"{self.name} is knocked out!")

  def lose_health(self, number):
    self.health -= number
    print(f"{self.name} lost {number} health, now has {self.health} health.")
    if self.health <= 0:
      self.knock_out()

  def regain_health(self, number):
    if self.health + number >= self.max_health:
      print(f"{self.name} gained {int(self.max_health - self.health)} health, is now on full health ({self.max_health})")
      self.health = self.max_health
    else:
      self.health += number
      print(f"{self.name} gained {number} health, now has {self.health} health.")