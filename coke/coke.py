
def ask_amount():
    return (int(input("Insert Coin: ")))


def main():
    amount_due = 50
    while amount_due >0:
        amount = ask_amount()
        if amount == 5 or amount == 10 or amount == 25:
            amount_due -= amount
        if amount_due <= 0:
            break
        print(f"Amount Due: {amount_due}")

    print(f"Change Owed: {abs(amount_due )}")


if __name__ == '__main__':
    main()
