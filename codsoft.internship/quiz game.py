import random

# Quiz questions and answers
quiz_questions = {
    "What is the capital of France?": "Paris",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the chemical symbol for water?": "H2O",
    "What is the largest planet in our solar system?": "Jupiter",
    "What is the powerhouse of the cell?": "Mitochondria"
}

# Function to present quiz questions
def present_quiz(questions):
    score = 0
    total_questions = len(questions)
    
    print("\nWelcome to the Quiz Game!")
    print("Here are the rules:")
    print("- You will be presented with multiple-choice questions.")
    print("- Select the correct answer.")
    print("- For each correct answer, you will earn one point.")
    print("- Let's get started!\n")
    
    # Shuffle the questions
    shuffled_questions = list(questions.items())
    random.shuffle(shuffled_questions)
    
    # Iterate through each question
    for i, (question, answer) in enumerate(shuffled_questions, 1):
        print(f"Question {i}: {question}")
        user_answer = input("Your answer: ").strip().capitalize()
        
        # Check if the answer is correct
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {answer}")
    
    return score, total_questions

# Function to display final results
def display_results(score, total_questions):
    percentage = (score / total_questions) * 100
    print("\nQuiz completed!")
    print(f"You answered {score} out of {total_questions} questions correctly.")
    print(f"Your final score: {score}/{total_questions} ({percentage:.2f}%)")
    if percentage >= 70:
        print("Congratulations! You passed the quiz.")
    else:
        print("Sorry, you did not pass the quiz. Better luck next time!")

# Main function to play the quiz
def play_quiz():
    while True:
        score, total_questions = present_quiz(quiz_questions)
        display_results(score, total_questions)
        
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break

# Run the quiz game
if _name_ == "_main_":
    play_quiz()
 

