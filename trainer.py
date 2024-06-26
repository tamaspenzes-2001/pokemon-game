import random
import time
import utils
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

  def __str__(self):
    string = f"\033[96m{self.name}\033[0;0m: "
    for pokémon in self.pokémons:
      string += str(pokémon)
      string += ", "
    return string[:-2]

  def heal_self(self):
    if self.healing_potions > 0:
      print(f"{self.name} healed themselves, has {self.healing_potions-1} healing potion(s) left.")
      self.regain_health(random.randint(1, 4))
      self.healing_potions -= 1
    else:
      print(f"{self.name} has no healing potions left!")

  def heal_pokémon(self):
    if self.healing_potions > 0:
      print(f"{self.name} healed {self.active_pokémon.name}, has {self.healing_potions-1} healing potion(s) left.")
      self.active_pokémon.regain_health(random.randint(1, 4))
      self.healing_potions -= 1
    else:
      print(f"{self.name} has no healing potions left!")

  def revive_pokémon(self, pokémon):
    if self.revive_potions > 0:
      pokémon.revive()
      self.revive_potions -= 1
      print(f"{self.name} revived {pokémon.name}, has {self.healing_potions} revive potion(s) left.")
      self.knocked_out_pokémons.remove(pokémon)
      self.pokémons.append(pokémon)
    else:
      print(f"{self.name} has no revive potions left!")

  def attack(self, other_trainer):
    attack_power = random.randint(1, 4) + self.level
    print(f"\n\033[96m{self.name}\033[0m attacked \033[95m{other_trainer.name}\033[0m, dealt \033[91m{attack_power}\033[0m damage.")
    self.gain_xp(attack_power)
    other_trainer.lose_health(attack_power)
    self.active_pokémon.attack(other_trainer.active_pokémon)
    if other_trainer.active_pokémon.knocked_out:
      other_trainer.active_pokémon_knocked_out(self)

  def gain_xp(self, damage_dealt):
    xp_earned = damage_dealt - (self.level / 2)
    self.xp += xp_earned
    print(f"\033[96m{self.name}\033[0m gained {xp_earned:g} xp, now has {self.xp:g} xp.")
    if self.xp >= self.level * 8:
      self.level_up()

  def level_up(self):
    self.level += 1
    self.health
    self.max_health += 1
    print(f"\033[96m{self.name}\033[0m leveled up, now is level {self.level}, gained 1 health and has {self.max_health} max health!")
    self.healing_potions += 1
    self.revive_potions += 1
    print(f"\033[96m{self.name}\033[0m won a healing and a revive potion, has {self.healing_potions} healing and {self.revive_potions} revive potion(s).")
      
  def active_pokémon_knocked_out(self, other_trainer):
    self.knocked_out_pokémons.append(self.active_pokémon)
    self.pokémons.remove(self.active_pokémon)
    if len(self.pokémons) == 0:
      print(f"\033[95m{self.name}\033[0m has no more pokémons left!")
      self.knock_out()

  def switch_pokémon(self, pokémon):
    self.active_pokémon = pokémon
    print(f"{pokémon.name} is now the active pokémon of {self.name}.")
    self.active_pokémon.print_stats()

  def print_stats(self):
    print(f"{self.name}: \033[96m{self.health:g}/{self.max_health}\033[0m health, \033[96m{self.xp:g}\033[0m xp, level \033[96m{self.level}\033[0m")

  def print_potions(self):
    print(f"{self.name} has \033[92m{self.healing_potions}\033[0m healing and \033[92m{self.revive_potions}\033[0m revive potions.")

  def print_pokémons(self):
    string = "Pokémon(s): "
    for pokémon in self.pokémons:
      string += str(pokémon)
      string += ", "
    print(string[:-2])

  def print_knocked_out_pokémons(self):
    if len(self.knocked_out_pokémons) > 0:
      string = "Knocked out pokémon(s): "
      for pokémon in self.knocked_out_pokémons:
        string += str(pokémon)
        string += ", "
      print(string[:-2])