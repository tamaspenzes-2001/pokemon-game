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

vulpix = Pokémon("Ninetales", "ice")
jynx = Pokémon("Jynx", "psychic")
dewgong = Pokémon("Dewgong", "ghost")

glacia = Trainer("Glacia", [vulpix, jynx, dewgong])

latias = Pokémon("Latias", "steel")
dragonite = Pokémon("Dragonite", "dragon")
gabite = Pokémon("Gabite", "grass")

drake = Trainer("Drake", [latias, dragonite, gabite])

trainers = [kabu, bruno, glacia, drake]

for i in range(6):
  kabu.attack(bruno)
  bruno.attack(kabu)
  print("")
  kabu.revive_pokémon(charmander)
  kabu.heal_pokémon()
  bruno.heal_pokémon()
  print("")