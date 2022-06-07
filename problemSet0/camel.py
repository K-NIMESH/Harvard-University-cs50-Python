def main():
    camel_case_var = get_input()
    snake_case_var = convert_var(camel_case_var)
    print("snake_case:", snake_case_var)


def get_input():
    user_input = input("camelCase: ")
    return user_input


def convert_var(text):
    for char in text:
        if char.isupper():
            text = text.replace(char, "_" + char.lower())
    return text


main()
