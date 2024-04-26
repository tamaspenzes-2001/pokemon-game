from pokemon import Pokémon
from trainer import Trainer
import time

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
    print_list(trainers)
    while True:
      user_choice = input(f"\033[7;49;9{i+2}mPlayer {i+1}\033[0;0m Choose a trainer (1-4):\n> ")
      if is_answer_valid(user_choice, len(trainers)):
        chosen_trainers.append(trainers.pop(int(user_choice)-1))
        break
  return chosen_trainers

def choose_new_active_pokémon(trainer):
  print("\033[32m" + "Your active pokémon is knocked out. Choose another one!" + "\033[0;0m")
  print_list(trainer.pokémons)
  while True:
    new_active_pokémon = input(f"> ")
    if is_answer_valid(new_active_pokémon, len(trainer.pokémons)):
      trainer.switch_pokémon(trainer.pokémons[int(new_active_pokémon)-1])
      break

def print_stats(trainer):
  trainer.print_stats()
  trainer.active_pokémon.print_stats()
  trainer.print_potions()

def choose_action(trainer):
  while True:
    print("\n\033[32m" + "What to do?" + "\033[0m")
    print("1. Heal active pokémon\n2. Revive a pokémon\n3. Attack")
    chosen_option = input("> ")
    if is_answer_valid(chosen_option, 3):
      match chosen_option:
        case "1": trainer.heal_pokémon()
        case "2":
          if trainer.revive_potions > 0:
            choose_pokémon_to_revive(trainer)
          else:
            print(f"{trainer.name} has no revive potions left!")
        case "3":
          choose_trainer_to_attack(trainer)
          break
        
def choose_pokémon_to_revive(trainer):
  if len(trainer.knocked_out_pokémons) == 0:
    print(trainer.name + " doesn't have any knocked out pokémons.")
    return
  print("\033[32m" + "Choose a knocked out pokémon to revive:" + "\033[0m")
  print_list(trainer.knocked_out_pokémons)
  while True:
    pokémon_to_revive = input(f"> ")
    if is_answer_valid(pokémon_to_revive, len(trainer.knocked_out_pokémons)):
      trainer.revive_pokémon(trainer.knocked_out_pokémons[int(pokémon_to_revive)-1])
      break

def choose_trainer_to_attack(attacker):
  other_trainers = [trainer for trainer in trainers if trainer.name != attacker.name]
  print("\033[32m" + "Choose a trainer to attack:" + "\033[0m")
  print_list(other_trainers)
  while True:
    trainer_to_attack = input(f"> ")
    if is_answer_valid(trainer_to_attack, len(other_trainers)):
      attacker.attack(other_trainers[int(trainer_to_attack)-1])
      break

def is_answer_valid(answer, number_of_options):
  try:
    answer_in_int = int(answer)
    if 0 < answer_in_int <= number_of_options:
      return True
    else:
      print("\033[91m" + "Invalid number!" + "\033[0m")
      return False
  except ValueError:
    print("\033[91m" + "Please provide a number!" + "\033[0m")
    return False

def print_list(list):
  for i in range(len(list)):
    print(str(i+1) + ". " + str(list[i]))

def main():
  global trainers
  print("Welcome gamers!\n")
  trainers = choose_characters(2)
  while True:
    for i in range(len(trainers)):
      trainer = trainers[i]
      print(f"\n\033[7;49;9{i+2}m{trainer.name}\033[0;0m")
      if trainer.active_pokémon.knocked_out:
        choose_new_active_pokémon(trainer)
        print("")
      print_stats(trainer)
      choose_action(trainer)
      time.sleep(2)

main()