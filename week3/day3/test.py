
# Exercise 7 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.




from faker import Faker  # import modules
import random

fake = Faker() #create fake person entity

users = [] #creates empty list for user list

def generate_fake_user(): #establish function to create the data for fake person
    user = {
        "name": fake.name(),
        "address": fake.address(),
        "language_code": random.choice(["en", "fr", "es", "de"])
    }
    return user

for _ in range(5): # generates 5 fake people and their info using a FOR loop
    user_data = generate_fake_user() #calling function that generates data
    users.append(user_data) #adds people to list users
    
for idx, user in enumerate(users, start=1): #for loop cycling through fake user index
    print(f"User {idx}:")
    print(f"Name: {user['name']}")
    print(f"Address: {user['address']}")
    print(f"Language Code: {user['language_code']}")
    print("\n")
    
    





