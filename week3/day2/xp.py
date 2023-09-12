# Create another cat breed named Siamese which inherits from the Cat class.
# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# Take all the cats for a walk, use the walk method.



class Pets(): #class called pets created
    def __init__(self, animals): #initiated with variable 'animals'
        self.animals = animals

    def walk(self): # method WALK created.  
        for animal in self.animals: #FOR loop that iterates through all pets
            print(animal.walk()) #lists who all walked?

class Cat(): #creating another class call Cat
    is_lazy = True #attribute that applies to the whole class is that cats are of course lazy

    def __init__(self, name, age): #method initiated with variables name and age
        self.name = name
        self.age = age

    def walk(self): #walk method specific to cats
        return f'{self.name} is just walking around'

class Bengal(Cat): # bengal class created
    def sing(self, sounds): #method SING with variable sounds
        return f'{sounds}' #makes the sounds

class Chartreux(Cat): # creates another class of cats that does the same thing
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
bengal_cat = Bengal("Bengal Cat", 3)
chartreux_cat = Chartreux("Chartreux Cat", 2)
siamese_cat = Siamese("Siamese Cat", 4)

all_cats = [bengal_cat, chartreux_cat, siamese_cat]
sara_pets = Pets(all_cats)
sara_pets.walk()



# Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.


class Dog: 
    def __init__ (self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        
    def bark(self):
        return f"{self.name} is barking"
        
    def run_speed(self):
        speed = self.weight / (self.age * 10)
        return speed
    
    def fight(self, other_dog):
        my_speed = self.run_speed() * self.weight
        other_speed = other_dog.run_speed() * other_dog.weight
        
        if my_speed > other_speed:
            return f"{self.name} won the fight!"
        elif my_speed < other_speed:
            return f"{other_dog.name} won the fight!"
        else:
            return "It's a draw!"
        
        
computer_dog = Dog("Computer", 833, 1)
belle_dog = Dog("Belle", 15, 8)
butchie_dog = Dog("Butchie", 45, 35)

print(computer_dog.bark())
print(f"{computer_dog.name}'s run speed: {computer_dog.run_speed()}")
print(belle_dog.fight(butchie_dog))

# Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.


import random #that has to be here in order to randomize the random.trick

class Dog: 
    def __init__ (self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        
    def bark(self):
        return f"{self.name} is barking"
        
    def run_speed(self):
        speed = self.weight / (self.age * 10)
        return speed
    
    def fight(self, other_dog):
        my_speed = self.run_speed() * self.weight
        other_speed = other_dog.run_speed() * other_dog.weight
        
        if my_speed > other_speed:
            return f"{self.name} won the fight!"
        elif my_speed < other_speed:
            return f"{other_dog.name} won the fight!"
        else:
            return "It's a draw!"
        
class PetDog (Dog): # this creates a child class adding the trained vairable defaulting to False
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained
    
    def train(self): 
        if not self.trained:
            print(f"{self.name} is now trained to bark!")
            self.trained = True
        else:
            print(f"{self.name} is already trained.")
        
    def play(self, *other_dogs): #the asterick opens it up to variable # of arguments
        dog_names = [dog.name for dog in other_dogs] #this gathers the other dogs
        dog_names.append(self.name)
        return f"{', '.join(dog_names)} all play together"
    
    def do_a_trick(self): #defining the trick function
        if self.trained: #making sure theyre trained first
            tricks = [ #makes a list of possible outcomes
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            random_trick = random.choice(tricks) #creates label for chosen trick
            print(random_trick)
        else:
            print(f"{self.name} is not trained :(") #if they arent trained
            
d1 = PetDog("Computer", 3000, 1)
d2 = PetDog("Belle", 15, 3)
d3 = PetDog("Butchie", 45, 35)

# d3.train()
# d2.do_a_trick()
result = d1.play(d2, d3)
print(result)
        

