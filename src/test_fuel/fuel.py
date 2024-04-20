def main():
    var = input("Enter a fraction in X/Y format: ")
    print(gauge(convert(var)))
# convert expects a str in X/Y format as input, wherein each of X and Y is an integer, 
# and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. 
# If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError. 
# If Y is 0, then convert should raise a ZeroDivisionError.


def convert (x: str) -> int:
    x, y = x.split("/")
    x, y = int(x), int(y)
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    if x > y:
        raise ValueError("X cannot be greater than Y")
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("X and Y must be integers")
    fraction = x / y
    percent = int(round(fraction * 100, 0))
    return percent

# gauge expects an int and returns a str that is:

#     "E" if that int is less than or equal to 1,
#     "F" if that int is greater than or equal to 99,
#     and "Z%" otherwise, wherein Z is that same int.

def gauge (x: int) -> str:
    if x <= 1:
        return "E"
    elif x >= 99:
        return "F"
    else:
        return f"{x}%"


if __name__ == '__main__':
    main()
