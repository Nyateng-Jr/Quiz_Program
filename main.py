# dictionary that stores answers and quizs
# a variable that tracks the score
# loop through the dictionary using the values pairs
# display each quiz to the player
# show result and score

quiz = {
    "question1": {
        "question": "What is the capital of Kenya?",
        "answer": "Nairobi"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the biggest continent?",
        "answer": "Africa"
    },
    "question4": {
        "question": "what is the capital of USA?",
        "answer": "Washington DC"
    },
    "question5": {
        "question": "what is the capital of Uganda?",
        "answer": "Kampala"
    }
}

score = 0
for key, value in quiz.items():
    print(value["question"])
    answer = input("Answer:")

    if answer.lower() == value["answer"].lower():
        print("Correct!")
        score = score + 1
        print("Your score is:" + str(score) + "\n")

    else:
        print("Wrong!")
        print("The correct answer is: " + value["answer"])
        print("Your score is:" + str(score) + "\n")

print("You got " + str(score) + " out of 5 questions.")
percentage = int(score/5*100)
print("Your % is " + str(percentage) + "%")
if percentage >= 40:
    print("Pass!")

else:
    print("Fail!")