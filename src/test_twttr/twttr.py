def main():
    response = input("Input: ")
    print(shorten(response))

def shorten(word):
    output = ""
    for i in word:
        check = i.lower()
        if check == 'a' or check == 'e' or check == 'i' or check == 'o' or check == 'u':
            continue
        # elif check == '1' or check == '2' or check == '3' or check == '4' or check == '5' or check == '6' or check == '7' or check == '8' or check == '9' or check == '0':
        #     continue
        else:
            output = output + i
    return output

if __name__ == '__main__':
    main()
