class Pokémon:
  multipliers = {
    0: ["normal-ghost", "electric-ground", "fighting-ghost", "poison-steel", "ground-flying", "psychic-dark", "ghost-normal", "dragon-fairy"]
    0.5: ["normal-rock", "normal-steel", "fire-fire", "fire-water", "fire-rock", "fire-dragon", "water-water", "water-grass", "water-dragon", "electric-electric", "electric-grass", "electric-dragon", "grass-fire", "grass-grass", "grass-poison", "grass-fly", "grass-bug", "grass-dragon", "grass-steel", "ice-fire", "ice-water", "ice-ice", "ice-steel", "fighting-poison", "fighting-flying", "fighting-psychic", "fighting-bug", "fighting-fairy", "poison-ground", "poison-rock", "poison-ghost", "ground-grass", "ground-bug", "flying-electric", "flying-rock", "flying-steel", "psychic-psychic", "psychic-steel", "bug-fire", "bug-fighting", "bug-poison", "bug-flying", "bug-ghost", "bug-steel", "bug-fairy", "rock-fighting", "rock-ground", "rock-steel", "ghost-dark", "dragon-steel", "dark-fighting", "dark-dark", "dark-fairy", "steel-fire", "steel-water", "steel-electric", "steel-steel", "fairy-fire", "fairy-poison", "fairy-steel"]
    2: ["fire-grass", "fire-ice", "fire-bug", "fire-steel", "water-fire", "water-ground", "water-rock", "electric-water", "electric-flying", "grass-water", "grass-ground", "grass-rock", "ice-grass", "ice-ground", "ice-fly", "ice-dragon", "fighting-normal", "fighting-ice", "fighting-rock", "fighting-dark", "fighting-steel", "poison-grass", "poison-fairy", "ground-fire", "ground-electric", "ground-poison", "ground-rock", "ground-steel", "flying-grass", "flying-fighting", "flying-bug", "psychic-fighting", "psychic-poisonous", "bug-grass", "bug-psychic", "bug-dark", "rock-fire", "rock-ice", "rock-flying", "rock-bug", "ghost-psychic", "ghost-ghost", "dragon-dragon", "dark-psychic", "dark-ghost", "steel-ice", "steel-rock", "steel-fairy", "fairy-fighting", "fairy-dragon", "fairy-dark"]
  }

  def __init__(self, name, level, pokémon_type):
    self.name = name
    self.level = level
    self.type = pokémon_type
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

  def regain_health(self, number):
    if self.health + number >= self.max_health:
      print(f"{self.name} gained {self.max_health - self.health} health, is now on full health ({self.max_health})")
      self.health = self.max_health
    else:
      self.health += number
      print(f"{self.name} gained {number} health, now has {self.health} health.")

  def attack(self, other_pokémon):
    for multiplier in Pokémon.multipliers:
      if f"{self.type}-{other_pokémon.type}" in Pokémon.multipliers[multiplier]:
        attack_multiplier = multiplier
        break
    attack_power = self.level * attack_multiplier
    print(f"{self.name} attacked {other_pokémon.name}, dealt {attack_power} damage.")
    other_pokémon.lose_health(attack_power)