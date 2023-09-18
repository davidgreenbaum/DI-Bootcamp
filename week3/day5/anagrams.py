import sys # allow us to fully exit the program if the user chooses
from anagram_checker import AnagramChecker  # Import the AnagramChecker class

def is_valid_input(word): # making sure user input is acceptable
    if len(word.split()) != 1: #cant be more than one word
        print("Error: Only a single word is allowed.")
        return False
    if not word.isalpha(): #can only accept letters
        print("Error: Only alphabetic characters are allowed.")
        return False
    return True

def main():
    print("Welcome to the Anagram Checker!")
    
    word_list_file = "sowpods.txt" #loads the txt file word list
    anagram_checker = AnagramChecker(word_list_file) #loads external python file
    
    while True:
        print("\nMENU:")
        print("1. Enter a word")
        print("2. Exit")
        
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == "1":
            word = input("Enter a word: ").strip() #get rid of spaces
            
            if is_valid_input(word): #calls function to check validity
                anagrams = anagram_checker.get_anagrams(word) #calls function in other file
                print(f"\nYOUR WORD: \"{word.upper()}\"")
                if anagram_checker.is_valid_word(word):
                    print("This is a valid English word.")
                    if anagrams:
                        print("Anagrams for you word", ", ".join(anagrams))
                    else:
                        print("No anagrams found for your word.") # if the word is valid but has no anagrams, it will let you know
                else:
                    print("This is not a valid English word.")
                print("Anagrams for your word:", ", ".join(anagrams))
        elif choice == "2": # exit option
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please choose 1 or 2.")

# this is a thing that lets it know what it the main script... so that when you import a module it know which is the main program and which is an imported module 
if __name__ == "__main__": 
    main()
