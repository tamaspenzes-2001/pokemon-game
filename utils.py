import os

def is_answer_valid(answer, max_number, min_number=1):
  try:
    answer_in_int = int(answer)
    if min_number <= answer_in_int <= max_number:
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

def clear_screen():
  os.system('cls' if os.name=='nt' else 'clear')