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
