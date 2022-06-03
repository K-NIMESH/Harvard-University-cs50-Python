# Harvard University's CS50-Python - 2022 Solutions

___

My version of the problem set answers from cs50p; an introduction to programming using Python, a popular language for general-purpose programming, data science, web programming, and more.

https://www.edx.org/course/cs50s-introduction-to-programming-with-python

___
### Problem Set 0: Functions, Variables 
___
#### 1. Indoor Voice

The a file called indoor.py, implements a program in Python that prompts the user for input and then outputs that same input in lowercase. 

#### 2. Playback Speed

The file called playback.py, implements a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

#### 3. Making Faces

The file called faces.py, implements a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

#### 4. Einstein

The file called einstein.py, implements a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

#### 5. Tip Calculator

The file called tip.py, implements a program in Python that prompts the user for a dollar amount and a percentage. Those values are converted into data types that can be evaluated together and produce a tip value. (i.e., $10.00 * 10% = $1.00)
___

### Problem Set 1: Conditionals

___
#### 1. Deep Thought

The file called deep.py, implements a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

#### 2. Home Federal Savings Bank

The file called bank.py, implements a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. The program will ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

#### 3. File Extensions

The file called extensions.py, implements a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of the common media type suffix. If the file’s name ends with some other suffix or has no suffix at all, the program will output application/octet-stream instead, which is a common default.

#### 4. Math Interpreter

The file called interpreter.py, implements a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. 

#### 4. Meal Time

The file called meal.py, implements a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time.

___

### Problem Set 2: Loops

___
#### 1. camelCase

The file called camel.py, implements a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. The program assumes that the user’s input will indeed be in camel case.

#### 2. Coke Machine

The file called coke.py, implements a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, the program will output how many cents in change the user is owed. The program will assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

#### 3. Just setting up my twttr

The file called twttr.py, implements a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

#### 4. Vanity Plates

The file called twttr.py, implements a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. 
- “All vanity plates must start with at least two letters.”
- “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
- “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
- “No periods, spaces, or punctuation marks are allowed.”
