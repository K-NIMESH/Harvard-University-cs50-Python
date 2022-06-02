def main():
    buy_coke()


def buy_coke():
    price = 50
    while price > 0:
        accepted_coins = [5, 10, 25]
        print("Amount Due:", price)
        user_input = int(input("Insert Coin:"))
        if user_input in accepted_coins:
            price = price - user_input
            if price <= 0:
                refund = abs(price)
                print("Change Owed: ", refund)


main()
