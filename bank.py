def main():
    greeting = getGreeting()
    amount = costOfGreeting(greeting)
    print(amount)

    
def getGreeting():
    userInput = input("Please Enter A Greeting: ").lower().replace(",", "")
    return userInput
    
    
def costOfGreeting(greeting):
    if greeting.split()[0] == "hello" and "hello" in greeting:
        return "$0"
    elif greeting.index("h") == 0:
        return "$20"
    else:
        return "$100"

        
main()
