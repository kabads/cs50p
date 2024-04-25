
while True:
    try: 
        x = int(input("What is x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")



def get_int(var_name):
    while True:
        try:
            return int(input(f"What is {var_name}? "))
        except ValueError:
            print("x is not an integer")

print(get_int("y"))
