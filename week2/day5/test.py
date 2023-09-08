# Challenge 2 : Longest Word
# Instructions
# Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
# Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).
# Examples

# longest_word("Margaret's toy is a pretty doll.") ➞ "Margaret's"

# longest_word("A thing of beauty is a joy forever.") ➞ "forever."

# longest_word("Forgetfulness is by all means powerless!") ➞ "Forgetfulness"


sentence = input("please enter a sentence for analysis: ") #get a sentence from user
words = sentence.split() # get rid of spaces and turn sentence into list of words
longest_word = "" # initiate empty variable for what will be the longest word
longest_length = 0 # initiate 0 value for what will be the calculated longest length

for word in words: # checking through each word in the newly created word list
    if len(word) > longest_length: #each word is checked against previous values
        longest_word = word # longest word gets descriptor
        longest_length = len(word) # longest length value gets descriptor
        
print("the longest word in the sentence : --", sentence, "-- is : ", longest_word, ".  it is ", longest_length, " characteres long!") #gives the user the results
    



