import random

# Quiz questions data
quiz_questions = {
    "What is the capital of India?": "Delhi",
    "What is the largest mammal in the world?": "Blue whale",
    "What is the national bird of India?": "Peacock",
    "What is the chemical symbol for water?": "H2O",
    "What is the powerhouse of the cell?": "Mitochondria"
}

def display_welcome_message():
    print("Welcome to the Quiz Game!")
    print("You will be asked multiple-choice or fill-in-the-blank questions.")
    print("Answer each question properly!")
    print("Let's get started...ALL THE BEST!!!\n")

# Function to present quiz questions
def present_quiz_questions():
    questions = list(quiz_questions.keys())
    random.shuffle(questions)
    score = 0
    
    for question in questions:
        print(question)
        user_answer = input("Your answer: ").strip().capitalize()
        correct_answer = quiz_questions[question]
        
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect! The correct answer is:", correct_answer)
    
    return score

# Function to display final results
def display_final_results(score, total_questions):
    print("\nQuiz Complete!")
    print("You answered", score, "out of", total_questions, "questions correctly.")
    print("Your final score is:", score, "/", total_questions)
    if score == total_questions:
        print("Congratulations! You got a perfect score!")
    elif score >= total_questions / 2:
        print("Well done! You passed the quiz!")
    else:
        print("Keep practicing! You can do better next time.")

# Function to play again
def play_again():
    choice = input("Do you want to play again? (yes/no): ").lower()
    return choice == "yes"

# Main function
def main():
    display_welcome_message()
    
    total_questions = len(quiz_questions)
    while True:
        score = present_quiz_questions()
        display_final_results(score, total_questions)
        if not play_again():
            break

if __name__ == "__main__":
    main()