def main():
    fraction = get_fraction()
    percent = int(round(fraction * 100, 0))
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")



def get_fraction():
    while True:
        try:
            fraction = input("Fraction: ").split('/')
            if int(fraction[0]) <= int(fraction[1]):
                divide = int(fraction[0]) / int(fraction[1])
            else:
                continue
            return divide
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


if __name__ == '__main__':
    main()
