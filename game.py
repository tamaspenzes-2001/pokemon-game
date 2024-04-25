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

# for i in range(6):
#   kabu.attack(bruno)
#   bruno.attack(kabu)
#   print("")
#   kabu.revive_pokémon(charmander)
#   kabu.heal_pokémon()
#   bruno.heal_pokémon()
#   print("")

def choose_characters(number_of_players):
  chosen_trainers = []
  for i in range(number_of_players):
    print("\033[32m" + "Available trainers and their pokémons:" + "\033[0;0m")
    for j in range(len(trainers)):
      print(str(j+1) + ". " + str(trainers[j]))
    while True:
      try:
        user_choice = int(input(f"\033[7;49;9{i+2}mPlayer {i+1}\033[0;0m Choose a trainer (1-4):\n> "))
        if 0 < user_choice <= len(trainers):
          chosen_trainers.append(trainers.pop(int(user_choice)-1))
          break
        else:
          print("\033[91m" + "Invalid number!" + "\033[0m")
      except ValueError:
        print("\033[91m" + "Please provide a number!" + "\033[0m")
  return chosen_trainers

def choose_new_active_pokémon(trainer):
  print("\033[32m" + "Your active pokémon is knocked out. Choose another one!" + "\033[0;0m")
  for i in range(len(trainer.pokémons)):
    print(str(i+1) + ". " + str(trainer.pokémons[i]))
  while True:
    try:
      new_active_pokémon = int(input(f"> "))
      if 0 < new_active_pokémon <= len(trainer.pokémons):
        trainer.switch_pokémon(trainer.pokémons[new_active_pokémon-1])
        break
      else:
        print("\033[91m" + "Invalid number!" + "\033[0m")
    except ValueError:
      print("\033[91m" + "Please provide a number!" + "\033[0m")

def main():
  print("Welcome gamers!\n")
  trainers = choose_characters(2)
  while True:
    for i in range(len(trainers)):
      trainer = trainers[i]
      print(f"\033[7;49;9{i+2}m{trainer.name}\033[0;0m")
      if trainer.active_pokémon.knocked_out:
        choose_new_active_pokémon(trainer)
        print("")
      trainer.print_health()
      trainer.active_pokémon.print_health()
      trainer.print_potions()

main()