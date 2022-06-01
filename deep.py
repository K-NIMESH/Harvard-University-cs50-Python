def main():
    userInput = input("What's the answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
    if greatAnswer(userInput):
        print("Yes")
    else:
        print("No")

def greatAnswer(userInput):
    if userInput == "42":
        return True
    elif "forty-two" in userInput:
        return True
    elif "forty two" in userInput:
        return True

main()
