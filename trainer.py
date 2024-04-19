import random
from character import Character

class Trainer(Character):
  def __init__(self, name, pokémons, potions):
    Character.__init__(self, name, 20)
    self.name = name
    self.pokémons = pokémons
    self.potions = potions
    self.active_pokémon = random.choice(pokémons)
    self.knocked_out_pokémons = []

  def heal_pokémon(self):
    if self.potions > 0:
      print(f"{self.name} healed {self.active_pokémon.name}, has {self.potions-1} potions left.")
      self.active_pokémon.regain_health(random.randint(1, 4))
      self.potions -= 1
    else:
      print(f"{self.name} has no potions left!")

  def attack(self, other_trainer):
    attack_power = random.randint(1, 4)
    print(f"{self.name} attacked {other_trainer.name}, dealt {attack_power} damage.")
    other_trainer.lose_health(attack_power)
    self.active_pokémon.attack(other_trainer.active_pokémon)
    if other_trainer.active_pokémon.knocked_out:
      other_trainer.active_pokémon_knocked_out()
      
  def active_pokémon_knocked_out(self):
    self.knocked_out_pokémons.append(self.active_pokémon)
    self.pokémons.remove(self.active_pokémon)
    self.switch_pokémon(random.choice(self.pokémons))

  def switch_pokémon(self, pokémon):
    self.active_pokémon = pokémon
    print(f"{pokémon.name} is now the active pokémon of {self.name}.")