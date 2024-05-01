from pokemon import Pokémon
from trainer import Trainer
import utils
import sys
import time

charmander = Pokémon("Charmander", "fire")
ninetales = Pokémon("Ninetales", "electric")
moltres = Pokémon("Moltres", "bug")

kabu = Trainer("Kabu", [charmander, ninetales, moltres])

mankey = Pokémon("Mankey", "fighting")
mewtwo = Pokémon("Mewtwo", "water")
tauros = Pokémon("Tauros", "fairy")

bruno = Trainer("Bruno", [mankey, mewtwo, tauros])

vulpix = Pokémon("Vulpix", "ice")
jynx = Pokémon("Jynx", "psychic")
dewgong = Pokémon("Dewgong", "ghost")

glacia = Trainer("Glacia", [vulpix, jynx, dewgong])

latias = Pokémon("Latias", "steel")
dragonite = Pokémon("Dragonite", "dragon")
gabite = Pokémon("Gabite", "grass")

drake = Trainer("Drake", [latias, dragonite, gabite])

tinkatuff = Pokémon("Tinkatuff", "dark")
kirlia = Pokémon("Kirlia", "normal")
altaria = Pokémon("Altaria", "poison")

mina = Trainer("Mina", [tinkatuff, kirlia, altaria])

bulbasaur = Pokémon("Bulbasaur", "ground")
ivysaur = Pokémon("Ivysaur", "flying")
weezing = Pokémon("Weezing", "rock")

koga = Trainer("Koga", [bulbasaur, ivysaur, weezing])

diglett = Pokémon("Diglett", "ice")
sandslash = Pokémon("Sandslash", "steel")
pikachu = Pokémon("Pikachu", "electric")

wattson = Trainer("Wattson", [diglett, sandslash, pikachu])

trainers = [kabu, bruno, glacia, drake, mina, koga, wattson]

def provide_number_of_players():
  while True:
    number_of_players = input(f"\nNumber of players (2-7)\n> ")
    if utils.is_answer_valid(number_of_players, 7, 2):
      return int(number_of_players)

def choose_trainers(number_of_players):
  chosen_trainers = []
  for i in range(number_of_players):
    print(f"\033[7;49;9{i+1}mPlayer {i+1}\033[0;0m")
    print("\033[32m" + "Choose a trainer:" + "\033[0;0m")
    utils.print_list(trainers)
    print("[Get pokémon damage by type: attacker-target (e.g. fire-water)]")
    while True:
      user_choice = input(f"> ")
      if "-" in user_choice:
        get_attack_power(user_choice)
      elif utils.is_answer_valid(user_choice, len(trainers)):
        chosen_trainers.append(trainers.pop(int(user_choice)-1))
        choose_active_pokémon(chosen_trainers[i])
        utils.clear_screen()
        break
  return chosen_trainers

def choose_active_pokémon(trainer):
  print("\033[32m" + "Choose a pokémon:" + "\033[0;0m")
  utils.print_list(trainer.pokémons)
  print("[Get pokémon damage by type: attacker-target (e.g. fire-water)]")
  while True:
    new_active_pokémon = input(f"> ")
    if "-" in new_active_pokémon:
      get_attack_power(new_active_pokémon)
    elif utils.is_answer_valid(new_active_pokémon, len(trainer.pokémons)):
      trainer.switch_pokémon(trainer.pokémons[int(new_active_pokémon)-1])
      break

def print_stats(trainer):
  trainer.print_stats()
  trainer.print_pokémons()
  trainer.active_pokémon.print_stats()
  trainer.print_knocked_out_pokémons()
  trainer.print_potions()

def choose_action(trainer):
  while True:
    print("\n\033[32m" + "What to do?" + "\033[0m")
    print("1. Heal active pokémon\n2. Revive a pokémon\n3. Change active pokémon\n4. Attack\n5. Get another player's stats")
    print("[Get pokémon damage by type: attacker-target (e.g. fire-water)]")
    chosen_option = input("> ")
    if "-" in chosen_option:
      get_attack_power(chosen_option)
    elif utils.is_answer_valid(chosen_option, 5):
      match chosen_option:
        case "1": trainer.heal_pokémon()
        case "2":
          if trainer.revive_potions > 0:
            choose_pokémon_to_revive(trainer)
          else:
            print(f"{trainer.name} has no revive potions left!")
        case "3": choose_active_pokémon(trainer)
        case "4":
          choose_trainer_to_attack(trainer)
          break
        case "5": choose_trainer_to_view_stats(trainer)
        
def choose_pokémon_to_revive(trainer):
  if len(trainer.knocked_out_pokémons) == 0:
    print(trainer.name + " doesn't have any knocked out pokémons.")
    return
  print("\033[32m" + "Choose a knocked out pokémon to revive:" + "\033[0m")
  utils.print_list(trainer.knocked_out_pokémons)
  while True:
    pokémon_to_revive = input(f"> ")
    if utils.is_answer_valid(pokémon_to_revive, len(trainer.knocked_out_pokémons)):
      trainer.revive_pokémon(trainer.knocked_out_pokémons[int(pokémon_to_revive)-1])
      break

def choose_trainer_to_attack(attacker):
  other_trainers = [trainer for trainer in trainers if trainer.name != attacker.name and not trainer.active_pokémon.knocked_out and not trainer.knocked_out]
  print("\033[32m" + "Choose a trainer to attack:" + "\033[0m")
  utils.print_list(other_trainers)
  while True:
    trainer_number = input(f"> ")
    if utils.is_answer_valid(trainer_number, len(other_trainers)):
      utils.clear_screen()
      attacker.attack(other_trainers[int(trainer_number)-1])
      print("")
      break

def choose_trainer_to_view_stats(current_trainer):
  other_trainers = [trainer for trainer in trainers if trainer.name != current_trainer.name and not trainer.knocked_out]
  print("\033[32m" + "Choose a trainer:" + "\033[0m")
  utils.print_list(other_trainers)
  while True:
    trainer_number = input(f"> ")
    if utils.is_answer_valid(trainer_number, len(other_trainers)):
      print_stats(other_trainers[int(trainer_number)-1])
      break

def get_attack_power(types):
  types_list = types.split("-")
  if len(types_list) == 2 and types_list[0] in Pokémon.pokémon_types and types_list[1] in Pokémon.pokémon_types:
    attack_multiplier = 1
    for multiplier in Pokémon.multipliers:
      if types in Pokémon.multipliers[multiplier]:
        attack_multiplier = multiplier
        break
    print(f"{types_list[0].title()} can deal \033[91m(level + 1) * {attack_multiplier}\033[0m damage to {types_list[1]}.")
  else:
    print("\033[91m" + "Invalid format or types!" + "\033[0m")

def check_game_state(number_of_players):
  counter = 0
  for trainer in trainers:
    if trainer.knocked_out:
      counter += 1
    else:
      not_knocked_out = trainer
  if counter+1 == number_of_players:
    sys.exit(f"\033[92m{not_knocked_out.name} won the game!\033[0m")

def main():
  global trainers
  print("Welcome gamers!")
  number_of_players = provide_number_of_players()
  utils.clear_screen()
  trainers = choose_trainers(number_of_players)
  while True:
    for i in range(len(trainers)):
      check_game_state(number_of_players)
      trainer = trainers[i]
      if trainer.knocked_out:
        continue
      print(f"\033[7;49;9{i+1}m{trainer.name}'s turn\033[0;0m")
      if trainer.active_pokémon.knocked_out:
        print(f"{trainer.name}'s active pokémon is knocked out.")
        choose_active_pokémon(trainer)
        print("")
      print_stats(trainer)
      choose_action(trainer)
      time.sleep(2)

main()