import validators

def validate(s):
    return validators.email(s)


def main():
    val = validate(input("What's your email address? "))
    if val == True:
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()