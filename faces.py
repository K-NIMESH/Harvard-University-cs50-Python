def main():
    text = input("Enter your Text. ")
    print(convert(text))

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