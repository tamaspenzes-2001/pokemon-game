import random

class Trainer:
  def __init__(self, name, pokémons, potions):
    self.name = name
    self.pokémons = pokémons
    self.potions = potions
    self.active_pokémon = random.choice(pokémons)

  def heal_pokémon(self):
    if self.potions > 0:
      print(f"{self.name} healed {self.active_pokémon.name}, has {self.potions-1} potions left.")
      self.active_pokémon.regain_health(random.randint(1, 4))
      self.potions -= 1
    else:
      print(f"{self.name} has no potions left!")