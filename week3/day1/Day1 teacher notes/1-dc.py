def find_biggest_word () :
    sentence = "I love programming in Python"
    list_words = sentence.split(" ")
    longest_word = list_words[0]
    for word in list_words :
        if len(word) > len(longest_word) :
            longest_word = word
    print(longest_word)

find_biggest_word()

# def find_smallest_word () :
#     sentence = "Emma loves programming in Python"
#     list_words = sentence.split(" ")
#     smallest_word = list_words[0]
#     for word in list_words :
#         if len(word) < len(smallest_word) :
#             smallest_word = word
#     print(smallest_word)

# find_smallest_word()

# def find_biggest_word () :
#     sentence = "Emma loves Pythons and she loves working from home"
#     list_words = sentence.split(" ")
#     longest_words = []
#     longest_word = list_words[0]
#     for word in list_words :
#         if len(word) > len(longest_word) :
#             longest_word = word
    
#     for word in list_words :
#         if len(word) == len(longest_word) :
#             longest_words.append(word)
    
#     print(longest_word)
#     print(longest_words)

# find_biggest_word()