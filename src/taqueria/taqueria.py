menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
def main():
  try:
    total = 0
    user_inputs = []
    while True:
      user_input = input("Enter a menu item: ").title()
      if user_input not in menu:
        continue
      total = total + menu[user_input]
      print(f"Total: ${total:,.2f}")
  except EOFError:
    pass


if __name__ == '__main__':
    main()