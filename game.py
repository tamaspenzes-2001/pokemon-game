from pokemon import Pokémon
from trainer import Trainer

charmander = Pokémon("Charmander", 10, "fire")
ninetales = Pokémon("Ninetales", 6, "fire")
moltres = Pokémon("Moltres", 8, "fire")

kabu = Trainer("Kabu", [charmander, ninetales, moltres], 5)

mankey = Pokémon("Mankey", 4, "fighting")
mewtwo = Pokémon("Mewtwo", 7, "fighting")
tauros = Pokémon("Tauros", 10, "fighting")

bruno = Trainer("Bruno", [mankey, mewtwo, tauros], 6)

kabu.attack(bruno)
bruno.attack(kabu)
kabu.heal_pokémon()
bruno.heal_pokémon()