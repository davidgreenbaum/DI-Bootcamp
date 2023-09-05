# Exercise 1 : Set
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers = {10, 11, 24}
my_fav_numbers.add(14)
my_fav_numbers.add(50)
my_fav_numbers.remove(50)
friend_fav_numbers = {2, 3, 4}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)


# 🌟 Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?

i believe you can, if its concatenated with another tuple of only integers




# 🌟 Exercise 3: List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.insert(0, "Kiwi")
total = (len(basket))
print(total)
basket.clear()
print(basket)


# 🌟 Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).


a float is a number with decimal places after it.  an integer is a whole number with no decimals after.  

list = [1.5]
for num in range(8):
    last_number = list[-1]
    new = last_number + .5
    list.append(new)
print(list)

# 🌟 Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.


my_list = [1]
for num in range(19) :
    last = my_list[-1]
    new = last + 1
    my_list.append(new)
for num in my_list :
    if num % 2 == 0 :
        my_list.pop(0)
print(my_list)

# couldnt figure out how to get it to loop propertly to show only the "even-index" numbers (which i think are the odd numbers to display)






# 🌟 Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

my_name = "david"
username = input("what is your name? ")
while username != my_name :
    username = input("what is your name ? ")
print("me too!")


# 🌟 Exercise 7: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

user_fruits = input("what are your favorite fruits? (and if you dont mind, separate the fruits with single space, no commas.) ")
fruit_list = list(user_fruits)
pick_fruit = input("name any fruit! ")
if pick_fruit == fruit_list :
    print("you picked one of your favorite fruits!")
else:
    print("not one of your favorites") 

# Exercise 8: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).





# i really struggled with this one and in the end used chat gpt to help.  i learned a lot... but definitely didnt figure this out on my own (google, notes)

toppings_list = []
total = 10

while True:
    toppings = input("what kind of toppings would you like? (type 'exit' to checkout) ")
    if toppings == "exit":
        break
   
    toppings_list.append(toppings) 
    total += 2.5
    
print(f"You've selected the following toppings: {', '.join(toppings_list)}")
print(f"Your total cost comes to ${total:.2f}")  








# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

INCOMPLETE
total_cost = 0
age_list = []
ages = input("what are the ages of the people in your family?")
for age in age_list:
    if age >= 3 and age <= 12:
        cost = 10
    elif age >12 :
        cost = 15
    else:
        cost = 0
    total_cost += cost
    
print (total_cost)





# Exercise 10 : Sandwich Orders
# Instructions
# Using the list below :

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
# We need to prepare the orders of the clients:
# Create an empty list called finished_sandwiches.
# One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
# I made your tuna sandwich
# I made your avocado sandwich
# I made your egg sandwich
# I made your chicken sandwich