# EXERCISE 1


# for i in range(10):
#     print(i)
    
# snippet 1- Time complexity would be O(1) because the amount of times it loops is independent of the the variable.  


# for i in range(n):
#     for j in range(n):
#         print(i, j)
        
        
# snippet 2 would be O(n) because the complexity directly correlates with the variable


# i = 1
# while i < n:
#     i *= 2
#     print(i)
    
    
# snippet 3 - the n value is the maximum times the loop happens because it stops once i reaches the value of n.  the multiplication within the loop is constant.  the unpredictable variable of n is what makes this O(n^2) 



# EXERCISE 2

# def insertion_sort(numbers: list) -> None: #creating the sorting function
#    for i in range(1, len(numbers)): # loop will start with second number in index
#       value = numbers[i] # defining value variable as i for current number being checked
#       j = i - 1 # defining j variable for the previous number
#       while value < numbers[j] and j >= 0: # what to do if previous number is bigger than previous
#          numbers[j + 1] = numbers[j] #they switch positions
#          j -= 1
#       numbers[j + 1] = value #moves to next index
    

# numbers = [5, 2, 9, 1, 5, 6] #provides list
   
# insertion_sort(numbers) # sorts the numbers list
# sorted_numbers = numbers.copy() #creates and labels newly sorted list
# print(sorted_numbers) 


# EXERCISE 3


numbers = [1, 3, 5, 7, 9, 11]

def binary_search(numbers: list, value: int) -> int: #defining function for doing binary search
    low = 0 
    high = len(numbers) - 1
    while low <= high: # what to do if low is smaller or eqal to high
        mid = int((low + high) / 2) # calculates average
        if numbers[mid] == value: #what to do if average/mid is the same as given value
            return mid
        elif numbers[mid] < value: #what to do if average/mid is less that given value
            low = mid + 1 # eliminate lower half of list
        else:
            high = mid - 1 #eliminate upper half of list
    return -1
   

binary_search(numbers, 7) # returns 3

index = binary_search(numbers, 7) #naming the result of the binary search

if index != -1: # what to do if value was found
  print("The value 7 was found at index {}.".format(index)) #displays index number
else: # what to do if value was not found
  print("The value 7 was not found in the list.")
