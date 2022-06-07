menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    get_order()


def get_order():
    total = 0
    while True:
        try:
            order = input("Item: ").title()
            total = total + menu[order]
            print("Total: ", "$","{:.2f}".format(total), sep="")
        except (ValueError,NameError,KeyError):
            pass
        except EOFError:
            return 0


main()
