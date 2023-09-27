def is_balanced(expr): # defining function to check parenthesis are properly placed

  stack = [] # initiates stack to keep track of parenthesis
  for char in expr: # creates for loop to iterate through characters within expr string
    if char in "([{": # what to do if it finds an opening parenthesis of any kind
      stack.append(char) # add that character to the stack we made
    elif char in ")]}": # what to do if it comes across a closing parenthesis
      if not stack or stack.pop() != char:  # checks for empty stack OR if it doesnt match whats in stack
        return False # then we have unbalanced parenthesis
    
    return not stack

# Example usage:

expr = "(1 + 2) * {[(3 / 4) - 5]}"
print(is_balanced(expr))  

expr = "[1 + 2) * (3 - 4)]"
print(is_balanced(expr))  

expr = "((1 + 2))"
print(is_balanced(expr))  

