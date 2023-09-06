# The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.
# Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.


data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def quiz () :
    num_right = 0
    num_wrong = 0
    for question_data in data:
        question = question_data["question"]
        correct_answer = question_data["answer"]
        ans = input(question + " ")
        if ans == correct_answer:
            num_right += 1
            print("correct!")
        else :
            num_wrong += 1
            print("wrong! the correct answer is ", correct_answer)
    print(f"you got " + str(num_right) + " answers correct!")
    print(f"but you got " + str(num_wrong) + " answers wrong.")
           
quiz ()
        
        
        