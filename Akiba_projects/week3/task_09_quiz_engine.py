
questions = [
    {
        "question": "Which language is commonly used for Python programming?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
        "answer": "A"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. String", "B. Boolean", "C. List", "D. Integer"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!--", "C. **", "D. #"],
        "answer": "D"
    },
    {
        "question": "Which data structure stores key-value pairs?",
        "options": ["A. Tuple", "B. Dictionary", "C. Set", "D. String"],
        "answer": "B"
    }
]


def display_question(question_data):
    print("\n" + question_data["question"])

    for option in question_data["options"]:
        print(option)


def validate_answer(answer):
    answer = answer.strip().upper()

    if answer in ["A", "B", "C", "D"]:
        return True

    return False


def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer


def update_score(score, is_correct):
    if is_correct:
        score = score + 1

    return score


def display_results(score, total_questions, correct, incorrect):
    percentage = (score / total_questions) * 100

    print("\n--- Final Quiz Results ---")
    print("Total questions:", total_questions)
    print("Correct answers:", correct)
    print("Incorrect answers:", incorrect)
    print("Final score:", score, "/", total_questions)
    print("Percentage:", format(percentage, ".2f"), "%")

    if percentage >= 80:
        print("Category: Excellent")
    elif percentage >= 60:
        print("Category: Good")
    elif percentage >= 40:
        print("Category: Fair")
    else:
        print("Category: Needs improvement")


def play_quiz():
    score = 0
    correct = 0
    incorrect = 0

    for question_data in questions:
        display_question(question_data)

        while True:
            user_answer = input("Enter your answer (A/B/C/D): ")

            if validate_answer(user_answer):
                user_answer = user_answer.strip().upper()
                break
            else:
                print("Invalid option! Please enter A, B, C, or D.")

        if check_answer(user_answer, question_data["answer"]):
            print("Correct!")
            correct = correct + 1
            score = update_score(score, True)
        else:
            print("Incorrect!")
            print("Correct answer:", question_data["answer"])
            incorrect = incorrect + 1
            score = update_score(score, False)

    display_results(score, len(questions), correct, incorrect)


def main():
    while True:
        print("\n=== Welcome to the Quiz ===")
        play_quiz()

        play_again = input("\nWould you like to play again? (yes/no): ")
        play_again = play_again.strip().lower()

        if play_again != "yes":
            print("Thank you for playing!")
            break


main()
