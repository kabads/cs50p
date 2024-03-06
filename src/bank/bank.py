
def greeting(question):
    response = input(question)
    return response.lower().strip()


def check(response):
    if response[0:5] == 'hello':
        print("$0")
    elif response[0] == 'h':
        print("$20")
    else:
        print("$100")


def main():
    user_greeting = greeting("Please offer a greeting")
    check(user_greeting)

if __name__ == '__main__':
    main()
