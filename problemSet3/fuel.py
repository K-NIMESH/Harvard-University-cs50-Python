def main():
    while True:
        try:
            result = get_frac("Fraction: ")
            fuel_gauge = check_max_min(result)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        except NameError:
            pass
        else:
            print(fuel_gauge)
            break


def get_frac(prompt):
    fraction = input(prompt).split("/")
    return abs(round(int(fraction[0]) / int(fraction[1]) * 100))


def check_max_min(number):
    if 99 <= number <= 100 :
        return "F"
    if number <= 1:
        return "E"
    if number > 100:
        return Error
    else:
        return f"{number}%"


main()
