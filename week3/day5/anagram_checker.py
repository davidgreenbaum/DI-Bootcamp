class AnagramChecker:
    def __init__(self, word_list_file):
        with open(word_list_file, 'r') as file:
            self.word_list = set(word.strip().lower() for word in file.readlines())
    
    def is_valid_word(self, word):
        return word.lower() in self.word_list
    
    def get_anagrams(self, word):
        word = word.lower()  # Convert the input word to lowercase
        anagrams = [w for w in self.word_list if sorted(w) == sorted(word) and w != word]
        return anagrams
    
    @staticmethod
    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

# Create an instance of AnagramChecker
anagram_checker = AnagramChecker("sowpods.txt")

word = "Listen"  # Now, you can use words with different cases
print(anagram_checker.is_valid_word(word))  # This will return True if "listen" is in the word list
print(anagram_checker.get_anagrams(word))
print(anagram_checker.is_anagram("Listen", "Silent"))  # This will return True as they are anagrams, ignoring case

