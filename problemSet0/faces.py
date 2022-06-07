def main():
    text = getText()
    convertedText = convert(text)
    print(convertedText)

    
def getText():    
    userInput = input("Enter your Text. ")   
    return userInput
    
def convert(string):
    if ":)" and ":(" in string:
        string = string.replace(":)", "🙂")
        string = string.replace(":(", "🙁")
        return string
    elif ":)" in string:
        string = string.replace(":)", "🙂")
        return string
    elif ":(" in string:
        string = string.replace(":(", "🙁")
        return string
    else:
        return string
main()
