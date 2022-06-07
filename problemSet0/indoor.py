def main():
  name = getLowercaseName()
  print(name)


def getLowercaseName():
  userInput = input("What's your name?").lower()
  return userInput


main()
