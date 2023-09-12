# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.




class Cat: #establing the class
    def __init__(self, cat_name, cat_age):  #assinging attributes
        self.name = cat_name  #naming the attributes
        self.age = cat_age
        
sad_cat = Cat("Sad", 4)  #creating instances and attributes
happy_cat = Cat("Happy", 5)
mean_cat = Cat("Mean", 2)
 
cats = [sad_cat, happy_cat, mean_cat] #turning it into a list

def find_oldest_cat(cats): #creating function for finding oldest cat
    oldest_cat = cats[0] #intializing variable for name of oldest cat
    oldest_age = cats[0].age #initalizing variable for age of oldest cat
    
    for cat in cats: #for loop to iterate through list
        if cat.age > oldest_age: #comparing each to what came before
            oldest_cat = cat 
            oldest_age = cat.age
    
    return f"The oldest cat is {oldest_cat.name} and is {oldest_age} years old."

result = find_oldest_cat(cats) #calls function and also creates "result"
print(result)




# Exercise 2 : Dogs
# Instructions
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.



class Dogs: #create class
    def __init__(self, name, height) : #initialize attributes
        self.name = name
        self.height = height
        
        
    def bark(self): #define bark function
        print(f"{self.name}, goes woof!")
        
    def jump(self): #define jump function
        jump_height = self.height * 2 #calculate jump height
        print (f"{self.name} jumps {jump_height} cm high!")
        

    
    
davids_dog = Dogs("Rex", 50) #create instance with attributes

print("The dogs name is ", davids_dog.name, "and he is ", davids_dog.height, "cm tall!")
davids_dog.bark()
davids_dog.jump()


sarahs_dog = Dogs("Teacup", 20)

print("The dogs name is ", sarahs_dog.name, "and he is ", sarahs_dog.height, "cm tall!")
sarahs_dog.bark()
sarahs_dog.jump()

    
# Exercise 3 : Who’s The Song Producer?
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


# Then, call the sing_me_a_song method. The output should be:

# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven


class Song: #creates class
    def __init__(self, lyrics) : # has the variable of self and lyrics
        self.lyrics = lyrics #naming
    def sing_me_a_song(self): #creating function for displaying song lyrics
        for line in self.lyrics: #FOR loop to display one "line" at a time
            print(line)
            
stairway = Song(["There's a lady who's sure", "all that glitters is gold", "and she's buying a stairway to heaven"])

stairway.sing_me_a_song()









# Exercise 4 : Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example

# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }


# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)



class Zoo :
    def __init__(self, zoo_name) :
        self.name = zoo_name
        self.animals = []
        pass
    
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} has been added to {self.name}'s animals.")
        else:
            print(f"{new_animal} is already in {self.name}'s animals")
    
    def get_animal(self):
        return self.animals
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animal:
            self.animals.remove(animal_sold)
            print(f"we have sold our " {animal_sold})
        else:            
            print(f"we dont have {animal_sold}")
        
    def sort_animals(self):
        sorted_animals = {}
        self.animals.sort()
        for animal in self.animals:
            first_letter = animal[0]
            if first_letter not in sorted_animals:
                sorted_animals[first_letter] = [animal]
            else:
                sorted_animals[first_letter].append(animal)
        for key, value in sorted_animals.items():
            print(f"{key}: {value}")
    
    def get_groups(self):
        sorted_animals = {}
        self.animals.sort()
        for animal in self.animals:
            first_letter = animal[0]  # Get the first letter of the animal name
            if first_letter not in sorted_animals:
                sorted_animals[first_letter] = [animal]
            else:
                sorted_animals[first_letter].append(animal)
        
        # Print animals inside each group
        for key, value in sorted_animals.items():
            print(f"{key}: {', '.join(value)}")

