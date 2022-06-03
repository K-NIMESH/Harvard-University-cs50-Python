fruit_facts = {
    "apple":130,
    "avocado":50,
    "banana":110,
    "cantaloupe":50,
    "grapefruit":60,
    "grapes":90,
    "honeydew melon":50,
    "kiwifruit":90,
    "lemon":15,
    "lime":20,
    "nectarine":60,
    "orange":80,
    "peach":60,
    "pear":100,
    "pineapple":50,
    "plums":70,
    "strawberries":50,
    "sweet cherries":100,
    "tangerine":50,
    "watermelon":80
}


def main():
    fruit = get_input()
    fruit_calories = get_calories(fruit)
    if fruit_calories != None: print("Calories:", fruit_calories)


def get_input():
    user_input = input("Item: ").lower()
    return user_input


def get_calories(string):
    if string in fruit_facts:
        return fruit_facts[string]
    return None

main()
