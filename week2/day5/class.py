data = [ #creating a dictionary to store the quiz questions and correct answers
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


def check_answers () : #creating a function running the quiz
    number_correct_answers = 0 #initialing bank for which are answered correctly
    number_incorrect_answers = 0 #initialize the bank for questions answered wrong
    list_wrong_answers = [] #initialize a list for saving users wrong answers

    print("\n ---- The quizz starts ----") #lets the user know we are starting
    for quizz in data : #beginning a FOR loop that will iterate through the quizz, question by question
        user_answer = input(quizz["question"]) #creation of bank for users guesses and prompts the question
        if user_answer.lower() == quizz["answer"].lower(): #setting condition what to do with right answer (making all letters lowercase)
            number_correct_answers += 1 #keep a tally of how many are answereed right
        else : #setting condition for wrong answer
            number_incorrect_answers += 1  #keeps tally of how many answered wrong
            new_quizz = quizz.copy() #dont totally get this, but its making a new dict so that og isnt altered
            new_quizz["user_answer"] = user_answer #naming the variable in new dictionary for users answer
            list_wrong_answers.append(new_quizz) #adding the wrong answers to new list
    
    inform_user(number_correct_answers, number_incorrect_answers, list_wrong_answers) #calling a function that is about to be created.  python preprocesses function definitions!

def inform_user (correct, incorrect, wrong_answers) : #establishing new function with three parameters
    print("\n ----------------------------") #visual clarity
    print(f"You have {correct} correct answers") # how many right
    print(f"You have {incorrect} incorrect answers") # how many wrong
    for global_answer in wrong_answers : #running a FOR loop but a little confused about these terms.  ------------
        print(f'The question was {global_answer["question"]}') # reviewing question
        print(f'Your answer was {global_answer["user_answer"]}') # showing wrong answer
        print(f'Your got it wrong, the correct answer is {global_answer["answer"]}') # showing right answer
    
    print("\n --------------------") #visual clarity
    if incorrect > 3 : # setting conditions for if they got too many wrong
        print(" YOU GOT MORE 3 ANSWERS WRONG Play Again") #inform them of consequence
        check_answers() # make them take quiz again
    else : # conditions if they did good enough
        print("Good Job - YOU DONT NEED TO REDO THE GAME") #congrats

check_answers() #not sure why this is here










