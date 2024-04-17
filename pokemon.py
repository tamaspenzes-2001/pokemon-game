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

  def revive(self):
    self.knocked_out = False
    self.health = self.max_health

  def lose_health(self, number):
    self.health -= number
    if self.health <= 0:
      self.knock_out()
