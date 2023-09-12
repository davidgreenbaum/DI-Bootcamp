# Create a Employee class, With the attributes : firstname, lastname, age, job, salary

# 1. Create 2 users object and display their attribute
# - Lea Smith 30 years old developer 25000 shekels
# - David Schartz 20 years old project manager 20000 shekels

# 2. Add those methods to the class
# - get_fullname(self) : that return the firstname + lastname
# - happy_birthday(self) : that return the age incremented by one
# - get_promotion(self, promotion_amount) : that increment the salary of the user by the promotion
# - show_info(self) : that will print the information of the employee --> name, age, job, salary

# 3. Call all the methods on the 2 objects

class Employee :
    def __init__(self, firstname, lastname, age, job, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.job = job
        self.salary = salary
    
    def get_fullname(self) :
        return f"{self.firstname} {self.lastname}"
    
    def happy_birthday(self):
        self.age += 1
    
    def get_promotion(self, new_promotion) :
        self.salary += new_promotion

    def show_info (self) :
        print(f"{self.get_fullname()} is {self.age} years old, his job is {self.job} and his salary is {self.salary}")
    
    
first_emp = Employee("Lea", "Smith", 30, "developer", 25000)
first_emp.show_info()
# Lea Smith is 30 years old, his job is developer and his salary is 25000
print(first_emp.get_fullname())
# Lea Smith'
print(first_emp.age)
# 30
first_emp.happy_birthday()
print(first_emp.age)
# 31
first_emp.show_info()
# Lea Smith is 31 years old, his job is developer and his salary is 25000
print(first_emp.salary)
# 25000
first_emp.get_promotion(2000)
print(first_emp.salary)
# 27000
first_emp.show_info()
# Lea Smith is 31 years old, his job is developer and his salary is 27000