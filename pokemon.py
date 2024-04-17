class Pokémon:
  def __init__(self, name, level, pokemon_type):
    self.name = name
    self.level = level
    self.type = pokemon_type
    self.max_health = level + 2
    self.health = self.max_health
    self.knocked_out = False