# Harvard University's CS50-Python - 2022 Solutions

___

My version of the problem set answers from cs50p; an introduction to programming using Python, a popular language for general-purpose programming, data science, web programming, and more.

[Harvard University's CS50-Python](https://www.edx.org/course/cs50s-introduction-to-programming-with-python)

___
### [Problem Set 0: Functions, Variables](https://github.com/alanbjordan/cs50-Python/tree/main/problemSet0)
___
#### [1. Indoor Voice](https://github.com/alanbjordan/cs50-Python/blob/main/problemSet0/indoor.py)

The a file called indoor.py, implements a program in Python that prompts the user for input and then outputs that same input in lowercase. 

#### [2. Playback Speed](https://github.com/alanbjordan/cs50-Python/blob/main/problemSet0/playback.py)

The file called playback.py, implements a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

#### [3. Making Faces](https://github.com/alanbjordan/cs50-Python/blob/main/problemSet0/faces.py)

The file called faces.py, implements a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

#### [4. Einstein](https://github.com/alanbjordan/cs50-Python/blob/main/problemSet0/einstein.py)

The file called einstein.py, implements a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

#### [5. Tip Calculator](https://github.com/alanbjordan/cs50-Python/blob/main/problemSet0/tip.py)

The file called tip.py, implements a program in Python that prompts the user for a dollar amount and a percentage. Those values are converted into data types that can be evaluated together and produce a tip value. (i.e., $10.00 * 10% = $1.00)
___

### [Problem Set 1: Conditionals](https://github.com/alanbjordan/cs50-Python/tree/main/problemSet1)

___
#### [1. Deep Thought](https://github.com/alanbjordan/cs50-Python/blob/main/problemSet1/deep.py)

The file called deep.py, implements a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

#### [2. Home Federal Savings Bank](https://github.com/alanbjordan/cs50-Python/blob/main/problemSet1/bank.py)

The file called bank.py, implements a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. The program will ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

#### [3. File Extensions](https://github.com/alanbjordan/cs50-Python/blob/main/problemSet1/extensions.py)

The file called extensions.py, implements a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of the common media type suffix. If the file’s name ends with some other suffix or has no suffix at all, the program will output application/octet-stream instead, which is a common default.

#### [4. Math Interpreter](https://github.com/alanbjordan/cs50-Python/blob/main/problemSet1/interpreter.py)

The file called interpreter.py, implements a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. 

#### [4. Meal Time](https://github.com/alanbjordan/cs50-Python/blob/main/problemSet1/meal.py)

The file called meal.py, implements a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time.

___

### [Problem Set 2: Loops](https://github.com/alanbjordan/cs50-Python/tree/main/problemSet2)

___
#### [1. camelCase](https://github.com/alanbjordan/cs50-Python/blob/main/problemSet2/camel.py)

The file called camel.py, implements a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. The program assumes that the user’s input will indeed be in camel case.

#### [2. Coke Machine](https://github.com/alanbjordan/cs50-Python/blob/main/problemSet2/coke.py)

The file called coke.py, implements a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, the program will output how many cents in change the user is owed. The program will assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

#### [3. Just setting up my twttr](https://github.com/alanbjordan/cs50-Python/blob/main/problemSet2/twttr.py)

The file called twttr.py, implements a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

#### [4. Vanity Plates](https://github.com/alanbjordan/cs50-Python/blob/main/problemSet2/plates.py)

The file called plates.py, implements a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. 
- “All vanity plates must start with at least two letters.”
- “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
- “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
- “No periods, spaces, or punctuation marks are allowed.”

#### [5. Nutrition Facts](https://github.com/alanbjordan/cs50-Python/blob/main/problemSet2/nutrition.py)

The file called nutrition.py, implements a program that prompts users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits. Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.

___

### Problem Set 3: Exceptions

___

#### 1. Fuel Gauge

The file called fuel.py, implements a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

#### 2. Felipe's Taqueria

The file called taqueria.py, implements a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, the program will display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. Program treats the user’s input case insensitively and ignores any input that isn’t an item. It assumes that every item on the menu will be titlecased.
