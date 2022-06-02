def main():
    buy_coke()


def buy_coke():
    price = 50
    while price > 0:
        accepted_coins = [5, 10, 25]
        print("Amount Due:", price)
        coin = int(input("Insert Coin:"))
        if coin in accepted_coins:
            price = price - coin
    else:
        print("Change Owed: ", abs(price))


main()
