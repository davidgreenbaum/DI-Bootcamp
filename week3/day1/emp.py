# Exercise 1 : Basic Classes
# Create a Employee class, With the attributes : firstname, lastname, age, job, salary

# 1. Create 2 users object and display their attribute
# - Lea Smith 30 years old developer 25000 shekels
# - David Schartz 20 years old project manager 20000 shekels

# 2. Add those methods to the class
# - get_fullname(self) : that return the firstname + lastname
# - (self) : that return the age incremented by one
# - get_promotion(self, promotion_amount) : that increment the salary of the user by the promotion
# - show_info(self) : that will print the information of the employee --> name, age, job, salary

# 3. Call all the methods on the 2 objects


class Employee :
    def __init__(self, firstname, lastname, age, job, salary) :
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.job = job
        self.salary = salary
        
        
        
lea_employee = Employee("Lea", "Smith", 30, "developer", 25000)
david_employee = Employee("David", "Schartz", 20, "project manager", 20000)

def get_fullname(self) :
    return f"{self.firstname}{self.lastname}"
    
def happy_birthday(self):
    self.age += 1
    return self.age

def get_promotion(self, new_promotion):
    self.salary += new_promotion
    
def show_info
    

    
    

    
    
    
# class Dog :

#     def __init__(self, dog_name, dog_age, dog_color = "black", dog_energy = 100) :
#         self.name = dog_name
#         self.age = dog_age
#         self.color = dog_color
#         self.energy = dog_energy
        
        
        
        
# lea_dog = Dog("Spock", 2)
# dan_dog = Dog("Rex", 4, "white")