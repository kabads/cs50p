"""Query the user what the answer to the meaning of life is.
If they say 42 or forty-two or forty two, then say Yes.
Otherwise say no@"""

def query(question):
    reply = input(question)
    return reply.strip()


def check(response):
    if response == "42" or response == "forty-two" or response == "forty two":
        print("Yes")
    else:
        print("No")

def main():
    response = query("What is the meaning of life?")
    check(response.lower())



if __name__ == '__main__':
    main()
