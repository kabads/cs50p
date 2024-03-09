def getExpression():
    return input("Expression: ")


def main():
    x, y, z = getExpression().split(' ')
    match y:
        case '+':
            print(round(float(int(x) + int(z)), 1))
        case '/':
            print(round(float(int(x) / int(z)), 1))
        case '-':
            print(round(float(int(x) - int(z)), 1))
        case '*':
            print(round(float(int(x) * int(z)), 1))

if __name__ == '__main__':
    main()
