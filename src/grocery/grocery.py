groceries = {}

def main():
  try:
    total = 0
    user_inputs = []
    while True:
      user_input = input().title()
      if user_input in groceries:
        groceries[user_input] += 1
      else:
        groceries[user_input] = 1
  except EOFError:
    sorted_groceries = dict(sorted(groceries.items()))
    for key, value in sorted_groceries.items():
      print(f'{value} {key.upper()}')



if __name__ == '__main__':
    main()