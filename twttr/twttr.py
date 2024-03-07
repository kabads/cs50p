


def main():
    response = input("Input: ")
    newresponse = ""
    for i in response:
        check = i.lower()
        if check == 'a' or check == 'e' or check == 'i' or check == 'o' or check == 'u':
            continue
        else:
            newresponse = newresponse + i

    print(newresponse)

if __name__ == '__main__':
    main()
