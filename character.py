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
    print(f"\033[95m{self.name}\033[0m is knocked out!")

  def lose_health(self, number):
    self.health -= number
    print(f"\033[95m{self.name}\033[0m lost \033[91m{number:g}\033[0m health, now has {self.health:g} health.")
    if self.health <= 0:
      self.knock_out()

  def regain_health(self, number):
    if self.health + number >= self.max_health:
      print(f"{self.name} gained {(self.max_health - self.health):g} health, is now on full health ({self.max_health})")
      self.health = self.max_health
    else:
      self.health += number
      print(f"{self.name} gained {number:g} health, now has {self.health:g} health.")