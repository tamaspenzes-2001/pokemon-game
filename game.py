from pokemon import Pokémon
from trainer import Trainer

charmander = Pokémon("Charmander", "fire")
ninetales = Pokémon("Ninetales", "electric")
moltres = Pokémon("Moltres", "bug")

kabu = Trainer("Kabu", [charmander, ninetales, moltres])

mankey = Pokémon("Mankey", "fighting")
mewtwo = Pokémon("Mewtwo", "water")
tauros = Pokémon("Tauros", "fairy")

bruno = Trainer("Bruno", [mankey, mewtwo, tauros])

for i in range(6):
  kabu.attack(bruno)
  bruno.attack(kabu)
  print("")
  kabu.revive_pokémon(charmander)
  kabu.heal_pokémon()
  bruno.heal_pokémon()
  print("")