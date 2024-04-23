from character import Character

class Pokémon(Character):
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
    print(f"{self.name} attacked {other_pokémon.name}, dealt {attack_power} damage.")
    if attack_power > 0:
      self.gain_xp(attack_power)
    other_pokémon.lose_health(attack_power)

  def gain_xp(self, damage_dealt):
    xp_earned = damage_dealt - (self.level / 2)
    self.xp += xp_earned
    print(f"{self.name} gained {xp_earned} xp, now has {self.xp} xp.")
    if self.xp >= self.level * 10:
      self.level += 1
      self.max_health += 1
      print(f"{self.name} leveled up, now is level {self.level} with {self.max_health} max health!")