def main():
    expression = getExpression()
    result = processExpression(expression)
    print(result)


def getExpression():
    userInput = input("Expression: ").split(" ")
    return userInput  


def processExpression(expression):
    x = int(expression[0])
    y = expression[1]
    z = int(expression[2])
    cal = calculate(x, y, z)
    calFloat = '%.2f' %cal
    result = removeLastValue(calFloat)
    return result


def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    elif operator == "**":
        return num1 ** num2
    elif operator == "//":
        return num1 // num2
    else:
        return "error"

    
def removeLastValue(x):
    convertedString = str(x)
    result = convertedString[:-1]
    return result


main()
