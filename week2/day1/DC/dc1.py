# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.
# If it’s 10 characters, print a message which states “perfect string” and continue the exercise.

# Then, print the first and last characters of the given text.

# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
# The user enters "HelloWorld"
# Then, you have to construct the string character by character
# H
# He
# Hel
# ... etc
# HelloWorld


# 4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:

# Hlrolelwod

string = input ( "please enter a 10 digit code of numbers and/or letters: ")
character_count = len(string)
if character_count < 10:
    print("code not long enough")
elif character_count > 10:
    print("code too long!")
else:
    print("perfect code")

first = string [0]
last = string [9]
print(f"{first} & {last}")
print(f"{string [0]}")
print(f"{string [1]}")
print(f"{string [2]}")
print(f"{string [3]}")
print(f"{string [4]}")
print(f"{string [5]}")
print(f"{string [6]}")
print(f"{string [7]}")
print(f"{string [8]}")
print(f"{string [9]}")

