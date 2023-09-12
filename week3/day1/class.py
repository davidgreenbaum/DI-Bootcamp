add comments in the play function

class Dog :

    def __init__(self, dog_name, dog_age, dog_color = "black", dog_energy = 100) :
        self.name = dog_name
        self.age = dog_age
        self.color = dog_color
        self.energy = dog_energy

    # method happybirthday increment the age by one
    def happy_birthday(self) :
        self.age += 1

    def show_info (self) :
        print(f"The dog name is {self.name}, his age is {self.age}, he is of color {self.color}")

    def go_to_groomer(self, owner_color) :
        self.color = owner_color

    def play (self, activity) : # creating function called play for the object based on variable called play
        if self.energy >= 10: #checking they have enough energy to play anything
            if self.energy >= 10 and activity == "ball" : # checking if enough energy to play ball
                self.energy -= 10 # subtract energy from that round
                print(f"{self.name} is playing ball - he has {self.energy} energy left") # print remaining energy
            elif self.energy >= 30 and activity == "frisbee": # checking if they have enough energy for frisbee
                self.energy -= 30 # subtracting fribee amount of energy
                print(f"{self.name} is playing frisbee - he has {self.energy} energy left") #print remaining energy
            elif self.energy >= 70 and activity.energy >= 70 and isinstance(activity, Dog) : #checking if both dogs have enough energy to play together in the event that, that is what is requested
                self.energy -= 70 #lea_dog energy
                activity.energy -= 70 #activity is dan_dog
                print(f"{self.name} and {activity.name} are playing together - {self.name} has {self.energy} energy left - - {activity.name} has {activity.energy} energy left") # print both dogs updated energy level
            else :
                print(f"You have {self.energy} left - You don't have enough energy to play {activity} \n") #what to do if not enough energy for the activity they chose
                self.play(input("Please choose another activity between ball, frisbee and play date \n")) # choose something else
        else :
            self.sleep() #if not enough energy for anything... calls the function sleep
    
    def sleep (self) : #creating SLEEP function to be applied to the object
        self.energy = 100 #updates the energy level regardless of previous level
        print(f"{self.name} slept, he has {self.energy} energy")  # updated energy level

lea_dog = Dog("Spock", 2)
dan_dog = Dog("Rex", 4, "white")
lea_dog.play(dan_dog)