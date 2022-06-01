def main():
    answer = getAnswer()
    if checkAnswer(answer):
        print("Yes")
    else:
        print("No")

        
def getAnswer(): 
    userInput = input("What's the answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
    return userInput


def checkAnswer(answer):
    if answer == "42":
        return True
    elif "forty-two" in answer:
        return True
    elif "forty two" in answer:
        return True

    
main()
