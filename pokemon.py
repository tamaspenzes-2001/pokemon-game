from character import Character

class Pokémon(Character):
  pokémon_types = ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"]
  multipliers = {
    0: ["normal-ghost", "electric-ground", "fighting-ghost", "poison-steel", "ground-flying", "psychic-dark", "ghost-normal", "dragon-fairy"],
    0.5: ["normal-rock", "normal-steel", "fire-fire", "fire-water", "fire-rock", "fire-dragon", "water-water", "water-grass", "water-dragon", "electric-electric", "electric-grass", "electric-dragon", "grass-fire", "grass-grass", "grass-poison", "grass-fly", "grass-bug", "grass-dragon", "grass-steel", "ice-fire", "ice-water", "ice-ice", "ice-steel", "fighting-poison", "fighting-flying", "fighting-psychic", "fighting-bug", "fighting-fairy", "poison-ground", "poison-rock", "poison-ghost", "ground-grass", "ground-bug", "flying-electric", "flying-rock", "flying-steel", "psychic-psychic", "psychic-steel", "bug-fire", "bug-fighting", "bug-poison", "bug-flying", "bug-ghost", "bug-steel", "bug-fairy", "rock-fighting", "rock-ground", "rock-steel", "ghost-dark", "dragon-steel", "dark-fighting", "dark-dark", "dark-fairy", "steel-fire", "steel-water", "steel-electric", "steel-steel", "fairy-fire", "fairy-poison", "fairy-steel"],
    2: ["fire-grass", "fire-ice", "fire-bug", "fire-steel", "water-fire", "water-ground", "water-rock", "electric-water", "electric-flying", "grass-water", "grass-ground", "grass-rock", "ice-grass", "ice-ground", "ice-fly", "ice-dragon", "fighting-normal", "fighting-ice", "fighting-rock", "fighting-dark", "fighting-steel", "poison-grass", "poison-fairy", "ground-fire", "ground-electric", "ground-poison", "ground-rock", "ground-steel", "flying-grass", "flying-fighting", "flying-bug", "psychic-fighting", "psychic-poisonous", "bug-grass", "bug-psychic", "bug-dark", "rock-fire", "rock-ice", "rock-flying", "rock-bug", "ghost-psychic", "ghost-ghost", "dragon-dragon", "dark-psychic", "dark-ghost", "steel-ice", "steel-rock", "steel-fairy", "fairy-fighting", "fairy-dragon", "fairy-dark"]
  }

  def __init__(self, name, pokémon_type):
    Character.__init__(self, name, 4)
    self.type = pokémon_type

  def __str__(self):
    return f"{self.name} ({self.type})"

  def revive(self):
    self.knocked_out = False
    self.health = self.max_health
    print(f"{self.name} is revived!")

  def attack(self, other_pokémon):
    attack_multiplier = 1
    for multiplier in Pokémon.multipliers:
      if f"{self.type}-{other_pokémon.type}" in Pokémon.multipliers[multiplier]:
        attack_multiplier = multiplier
        break
    attack_power = (self.level + 1) * attack_multiplier
    print(f"\033[96m{self}\033[0m attacked \033[95m{other_pokémon}\033[0m, dealt \033[91m{attack_power:g}\033[0m damage.")
    if attack_power > 0:
      self.gain_xp(attack_power)
    other_pokémon.lose_health(attack_power)

  def gain_xp(self, damage_dealt):
    xp_earned = damage_dealt - (self.level / 2)
    self.xp += xp_earned
    print(f"\033[96m{self.name}\033[0m gained {xp_earned:g} xp, now has {self.xp:g} xp.")
    if self.xp >= self.level * 10:
      self.level += 1
      self.max_health += 1
      print(f"\033[96m{self.name}\033[0m leveled up, now is level {self.level} with {self.max_health} max health!")

  def print_stats(self):
    print(f"{self}: \033[96m{self.health:g}/{self.max_health}\033[0m health, \033[96m{self.xp:g}\033[0m xp, level \033[96m{self.level}\033[0m")