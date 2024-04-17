class Pokémon:
  def __init__(self, name, level, pokemon_type):
    self.name = name
    self.level = level
    self.type = pokemon_type
    self.max_health = level + 2
    self.health = self.max_health
    self.knocked_out = False

  def knock_out(self):
    self.knocked_out = True
    print(f"{self.name} is knocked out!")

  def revive(self):
    self.knocked_out = False
    self.health = self.max_health
    print(f"{self.name} is revived!")

  def lose_health(self, number):
    self.health -= number
    print(f"{self.name} lost {number} health, now has {self.health} health.")
    if self.health <= 0:
      self.knock_out()
