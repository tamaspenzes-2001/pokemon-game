import random
import sys
from character import Character

class Trainer(Character):
  def __init__(self, name, pokémons):
    Character.__init__(self, name, 20)
    self.name = name
    self.pokémons = pokémons
    self.healing_potions = 1
    self.revive_potions = 1
    self.active_pokémon = random.choice(pokémons)
    self.knocked_out_pokémons = []

  def heal_pokémon(self):
    if self.healing_potions > 0:
      print(f"{self.name} healed {self.active_pokémon.name}, has {self.healing_potions-1} potions left.")
      self.active_pokémon.regain_health(random.randint(1, 4))
      self.healing_potions -= 1
    else:
      print(f"{self.name} has no healing potions left!")

  def revive_pokémon(self, pokémon):
    if pokémon in self.knocked_out_pokémons and self.revive_potions > 0:
      pokémon.revive()
      self.knocked_out_pokémons.remove(pokémon)
      self.pokémons.append(pokémon)
    elif pokémon not in self.knocked_out_pokémons:
      print(f"{pokémon.name} isn't knocked out!")
    else:
      print(f"{self.name} has no revive potions left!")

  def attack(self, other_trainer):
    attack_power = random.randint(1, 4)
    print(f"{self.name} attacked {other_trainer.name}, dealt {attack_power} damage.")
    self.gain_xp(attack_power)
    other_trainer.lose_health(attack_power)
    self.active_pokémon.attack(other_trainer.active_pokémon)
    if other_trainer.active_pokémon.knocked_out:
      other_trainer.active_pokémon_knocked_out(self)

  def gain_xp(self, damage_dealt):
    xp_earned = damage_dealt - (self.level / 2)
    self.xp += xp_earned
    print(f"{self.name} gained {xp_earned} xp, now has {self.xp} xp.")
    if self.xp >= self.level * 15:
      self.level += 1
      self.max_health += 1
      print(f"{self.name} leveled up, now is level {self.level} with {self.max_health} max health!")
      self.healing_potions += 1
      self.revive_potions += 1
      print(f"{self.name} won a healing and a revive potion, has {self.healing_potions} healing and {self.revive_potions} revive potions.")
      
  def active_pokémon_knocked_out(self, other_trainer):
    self.knocked_out_pokémons.append(self.active_pokémon)
    self.pokémons.remove(self.active_pokémon)
    if len(self.pokémons) > 0:
      self.switch_pokémon(random.choice(self.pokémons))
    else:
      print(f"{self.name} has no more pokémons left!")
      self.knock_out()
      sys.exit(f"{other_trainer} won the game!")

  def switch_pokémon(self, pokémon):
    self.active_pokémon = pokémon
    print(f"{pokémon.name} is now the active pokémon of {self.name}.")