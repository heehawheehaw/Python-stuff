###
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter(A, B, C, or D):")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
    
    display_score(correct_guesses,guess)
###
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0 

###
def display_score(correct_guesses, guesses):
    print("-----------------------")
    print("RESULTS")
    print("----------------------")
    print("Answer:", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses:", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is : " +str(score)+"%")
###
def play_again():
    response = input("do you want to play again?: (yes or no): ")
    response = response.upper()
    if response =="YES":
        return True
    else:
        return False

        
questions = {#dictionary
    "YOur Mum gAy?: ": "A",
    "WhY iS YoUr Mum GaY?": "D",
    "AllahGang?:":"B"
    "Who is Joe?" : "C"
}
options=[#2d list
    ["A. Yes","B. NO","C. Maybe","D. donthavemumlel"],
    ["A. IDK","B. duetofather","C. Allherlifeshehadtohideit","D. satanworshipper"],
    ["A. Yes","B. no(aethist)","C. no(christian)","D. wallahi"],
    ["A. JOMAMA","B. asdf", "C. asdf","D. asdf"]
]

new_game()

while play_again():
    new_game()

print("Bye!")