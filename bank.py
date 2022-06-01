def main():
    greeting = input("Please Enter A Greeting: ").lower().replace(",", "")
    costOfGreeting(greeting)


def costOfGreeting(greeting):
    if greeting.split()[0] == "hello" and "hello" in greeting:
        print("$0")
    elif greeting.index("h") == 0:
        print("$20")
    else:
        print("$100")

        
main()
