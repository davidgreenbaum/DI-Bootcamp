# Exercise 2: Import
# Instructions
# In a file named func.py create a function that adds 2 number, and prints the result
# In a file namedexercise_one.py import and the function
# Hint: You can use the the following syntaxes:

# import module_name 

# OR 

# from module_name import function_name 

# OR 

# from module_name import function_name as fn 

# OR

# import module_name as mn

from func import add_numbers #imports method from other .py file in same folder

num1 = 5  #providing variables
num2 = 2000

add_numbers(num1, num2) #calling the method 
