
# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.

# Take the random words and create a sentence (using a python method), the sentence should be lower case.

# Create a function called main which will:

# Print a message explaining what the program does.

# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.

import random

def get_words_from_file(file_path):
    words = [] #initializing empty word list
    user_num = 0
    
    try:
        with open(file_path, 'r') as file: #open the file in read mode
            words = file.read().splitlines() #names the content thats being read
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return words
    
def get_random_sentence(words, length):
    if length <= 0:
        print("please enter a higher number")
    else:
        random_sentence = ' '.join(random.sample(words, length))
        print("Random sentence:", random_sentence)
        
file_path = "sowpods.txt"
words = get_words_from_file(file_path)

if words:
    user_length = int(input("I'm going to make a random sentence.  How many words long would you like it to be?"))
    get_random_sentence(words, user_length)


# Exercise 2: Working With JSON
# Instructions
# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.


import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson) #turns it into a dictionary

salary = data["company"]["employee"]["payable"]["salary"] #points to salary
print("Salary:", salary) 

data["company"]["employee"]["birth_date"] = "1989-12-09" #adds a birthday

modifiedJson = json.dumps(data, indent=4) #changes it back to JSON

with open("modified_data.json", "w") as json_file: #saves it to an external file
    json_file.write(modifiedJson)
    
print("Modified JSON saved to 'modified_data.json") # wow