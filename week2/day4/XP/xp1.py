# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.


def display_message() :
    print("I am learning how to CODE.")
    
display_message()



# 🌟 Exercise 2: What’s Your Favorite Book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.

def favorite_book (title) :
    print("one of my favorite books is called " + title)
    
favorite_book("Life of Pi")


# Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.

def describe_city(city, country="the universe") :
    print(city + " is in " + country)
    
describe_city ("Jerusalem", "Israel")

# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

import random

def compare_numbers (user_num) :
    rand_num = random.randint(1, 100)
    if user_num == rand_num:
        print("Success!")
    else :
        print("Fail!" + "   You number was " + str(user_num) + " and the random number was " + str(rand_num))
        
compare_numbers (35)


# Exercise 5 : Let’s Create Some Personalized Shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.

# Bonus: Call the function make_shirt() using keyword arguments.


# first function

def make_shirt (size, text) :
    print("the size of the shirt is " + size + ".  and the text is " + text)
    
make_shirt("XL", "HAPPY BIRTHDAY")





# large shirt, default message

def make_shirt (size="L", text="i love python") :
    print("the size of the shirt is " + size + ".  and the text is " + text)
    
make_shirt()




# medium shirt, default message

def make_shirt (size="L", text="i love python") :
    print("the size of the shirt is " + size + ".  and the text is " + text)
    
make_shirt("M",)



# any size, different message

def make_shirt (size="L", text="i love python") :
    print("the size of the shirt is " + size + ".  and the text is " + text)
    
make_shirt("S", "i love html")




# Exercise 6 : Magicians …
# Instructions
# Using this list of magician’s names

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Create a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.


magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians() :
    print(magician_names)
    
show_magicians()

def make_great() :
    for i in range(len(magician_names)):
        magician_names[i] += " the Great"
        
make_great()
show_magicians()

# i needed a lot of internet help with this one.  i'm still not totally familiar with the range(len) part and the [i] += " the Great.  i didnt come up with those on my own.  




# Exercise 7 : Temperature Advice
# Instructions
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.

# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40

# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().

# Bonus: Give the temperature as a floating-point number instead of an integer.
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.


import random

season = input("pick a season (summer, spring, winter, or fall: ")

def get_random_temp(season) :
    if season == "fall" :
        rand_temp = random.randint(35, 65)
    elif season == "summer" :
        rand_temp = random.randint(80, 120)
    elif season == "spring" :
        rand_temp = random.randint(66, 79)
    elif season == "winter" :
        rand_temp = random.randint(0, 45)
    print("the temperature outside is " + str(rand_temp))
    return rand_temp
    
get_random_temp(season)            
        
    # rand_temp = random.randint(-1, 110)
    # print(rand_temp)
    # return rand_temp

# def main() :
#     rand_temp = get_random_temp()
#     print("the temperature outside right now is " + str(rand_temp) + " degrees celcius")
#     if rand_temp < 0 :
#         print("burrr thats freezing!")
#     elif 0 <= rand_temp < 16 :
#         print("quite chilly!")
#     elif 16 <= rand_temp <= 23 :
#         print("i dont know celcius but sounds nice!")
#     elif 24 <= rand_temp <= 32 :
#         print("thats something!")
#     else :
#         print("its a hot one!")
    
# main("", 3)




# Exercise 5 : Star Wars Quiz
# Instructions
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

# Here is an array of dictionaries, containing those questions and answers

data = [
{
    "question": "What is Baby Yoda's real name?",
    "answer": "Grogu"},
{
    "question": "Where did Obi-Wan take Luke after his birth?",
    "answer": "Tatooine"
},
{
    "question": "What year did the first Star Wars movie come out?",
    "answer": "1977"
},
{
    "question": "Who built C-3PO?",
    "answer": "Anakin Skywalker"
},
{
    "question": "Anakin Skywalker grew up to be who?",
    "answer": "Darth Vader"
},
{
    "question": "What species is Chewbacca?",
    "answer": "Wookiee"
}
]


# Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.



def quiz () :
    num_right = 0
    num_wrong = 0
    for question_data in data:
        question = question_data["question"]
        correct_answer = question_data["answer"]
        ans = input(question + " ")
        if ans == correct_answer:
            num_right += 1
            print("correct!")
        else :
            num_wrong += 1
            print("wrong! the correct answer is ", correct_answer)
    print(f"you got " + str(num_right) + " answers correct!")
    print(f"but you got " + str(num_wrong) + " answers wrong.")
           
quiz ()