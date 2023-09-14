# Instructions :
# The goal of the exercise is to create a class that will help you analyze a specific text. A text can be just a simple string, like “Today, is a happy day” or it can be an external text file.
# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code

# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.


# Part II
# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.

# Implement a classmethod that returns a Text instance but with a text file:

#     >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.


# Now, use the provided the_stranger.txt file and try using the class you created above.


class Text: # creating class where text string can be taken as an argument
    def __init__(self, text) :
        self.text = text
    
    def word_frequency(self, word): # splits out the individual words
        words = self.text.split() #names the list
        word_counts = {} #intitialize empty dictionary
        for word in words:
            if word in word_counts: # what to do if the word is already in the dictionary
                word_counts[word] += 1 # add to existing quanity
            else:
                word_counts[word] = 1 # if its not in dictionary, add it
        if word_counts:
            return max(word_counts, key=word_counts.get) #finds most common word
        else:
            return None
        
    def most_common_word(self): # creating function to find most frequent word used
        words = self.text.split() #splits up the individual words
        word_counts = {} #initializing empty dictionary 
        for word in words: #iterating through list of words
            if word in word_counts:
                word_counts[word] += 1 #if the word has already been counted its added to existing
            else:
                word_counts[word] = 1 #otherwise it gets the quantity of one
        if word_counts:
            return max(word_counts, key=word_counts.get) #identifies most frequently used word
        else:
            return None
        
    def unique_words(self): #creating function to identify unique words
        words = self.text.split() #splits the words up individually
        unique_words = set(words) #creates label for unique words
        return list (unique_words)
    
    def from_file(cls, filename): 
        with open(filename, 'r', encoding='utf-8') as file:
            file_text = file.read()
        return cls(file_text)
        
text_string = "I wonder what an interesting sentence coming from my mind full of wonder could be interesting or if my mind will not think the sentence is interesting or have any wonder at all."
text_instance = Text(text_string)
print(text_instance.word_frequency("interesting"))  
print(text_instance.most_common_word())  
print(text_instance.unique_words())  
