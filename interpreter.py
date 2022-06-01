def main():

    ns = input("Expression: ").split(" ")

    x = int(ns[0])

    y = ns[1]

    z = int(ns[2])

    cal = calculate(x, y, z)

    calFloat = '%.2f' %cal

    result = remLastVal(calFloat)

    print(result)

def calculate(num1, op, num2):

    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    elif op == "%":
        return num1 % num2
    elif op == "**":
        return num1 ** num2
    elif op == "//":
        return num1 // num2
    else:
        return "error"

def remLastVal(x):
    vert = str(x)
    newVert = vert[:-1]
    return newVert

main()