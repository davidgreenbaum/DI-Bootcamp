# str
#     - methods :
#         upper()
#         lower()
    
# "hello"

# --> object of the class str
# --> it inherits all the methods of the class str


# "hello".upper()

class Dog :

    # method
    def drink_water(self) :
        print("The dog is drinking water")


# i create a Dog object
# i create a Dog instance
# an object is an instance of a class
my_dog = Dog()
my_dog.drink_water()


class Dog :
    # double underscore
    # used to initialize the instance attributes
    def __init__(self, dog_name) :
        self.name = dog_name
        # name is an attribute

    # method
    def drink_water(self) :
        print("The dog is drinking water")

# the init method is called automatically when we create a new object
my_dog = Dog("Rex")
print(f"my dog name is {my_dog.name}")
my_dog.drink_water()

lea_dog = Dog("Spock")
print(f"the name of lea's dog is {lea_dog.name}")
print(lea_dog)
print(lea_dog.__dict__)
print(dir(lea_dog))


class Dog :

    def __init__(self, dog_name, dog_age) :
        self.name = dog_name
        self.age = dog_age
        self.color = "black"

    # method happybirthday increment the age by one
    def happy_birthday(self) :
        self.age += 1

lea_dog = Dog("Spock", 2)
print(lea_dog.__dict__)

dan_dog = Dog("Rex", 4)
dan_dog.color = "white"
print(dan_dog.__dict__)

# ---------------------------

class Dog :

    def __init__(self, dog_name, dog_age, dog_color = "black") :
        self.name = dog_name
        self.age = dog_age
        self.color = dog_color

    # method happybirthday increment the age by one
    def happy_birthday(self) :
        self.age += 1

    def show_info (self) :
        print(f"The dog name is {self.name}, his age is {self.age}, he is of color {self.color}")

    def go_to_groomer(self, owner_color) :
        self.color = owner_color


lea_dog = Dog("Spock", 2)
lea_dog.go_to_groomer("pink")
lea_dog.show_info()

dan_dog = Dog("Rex", 4, "white")
dan_dog.show_info()

lea_dog.happy_birthday()
print(f"the age of lea's dog is {lea_dog.age}")

