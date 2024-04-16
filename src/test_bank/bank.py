def value(response) -> int:
    response = response.lower().strip()
    if response[0:5] == 'hello':
        return 0
    elif response[0] == 'h':
        return 20
    else:
        return 100


def main():
    user_greeting = input("Please offer a greeting")
    print(f"${value(user_greeting)}")

if __name__ == '__main__':
    main()
