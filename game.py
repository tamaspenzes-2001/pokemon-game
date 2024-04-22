from pokemon import Pokémon
from trainer import Trainer

charmander = Pokémon("Charmander", "fire")
ninetales = Pokémon("Ninetales", "electric")
moltres = Pokémon("Moltres", "bug")

kabu = Trainer("Kabu", [charmander, ninetales, moltres], 5)

mankey = Pokémon("Mankey", "fighting")
mewtwo = Pokémon("Mewtwo", "water")
tauros = Pokémon("Tauros", "fairy")

bruno = Trainer("Bruno", [mankey, mewtwo, tauros], 6)

kabu.attack(bruno)
bruno.attack(kabu)
kabu.heal_pokémon()
bruno.heal_pokémon()