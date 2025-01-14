import sys

def main():
    # List of questions (dictionary format)
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["1. Paris", "2. London", "3. Berlin", "4. Madrid"],
            "answer": 1,
        },
        {
            "question": "What is 5 + 7?",
            "options": ["1. 10", "2. 12", "3. 14", "4. 15"],
            "answer": 2,
        },
         {
            "question": "Who is the CEO of Google?",
            "options": ["1. Sundar Pichai", "2. Tim Cook", "3. Jeff Bezos", "4. Elon Musk"],
            "answer": 1,
        },
          {
            "question": "What is the capital of India?",
            "options": ["1. Mumbai", "2. New Delhi", "3. Kolkata", "4. Chennai"],
            "answer": 2,
        },
           {
            "question": "What is 6 * 8?",
            "options": ["1. 42", "2. 48", "3. 56", "4. 64"],
            "answer": 2,
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["1. Harper Lee", "2. J.K. Rowling", "3. Mark Twain", "4. Ernest Hemingway"],
            "answer": 1,
        },
         {
            "question": "What is the largest mammal in the world?",
            "options": ["1. Elephant", "2. Blue Whale", "3. Giraffe", "4. Hippopotamus"],
            "answer": 2,
        },
    ]

    score = 0  # Initialize score
    print("\nWelcome to the Quiz App 🧠\n")

    for idx, q in enumerate(questions):
        print(f"Question {idx + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        print("Enter the option number (1-4) or 's' to skip, 'e' to exit.")

        user_input = input("> ").strip().lower()

        if user_input == "s":
            print("Skipped!\n")
            continue
        elif user_input == "e":
            print("Exiting the quiz...")
            break
        elif user_input.isdigit() and 1 <= int(user_input) <= 4:
            if int(user_input) == q["answer"]:
                print("Correct! 🎉\n")
                score += 1
            else:
                print("Wrong! 😔\n")
        else:
            print("Invalid input. Please try again.\n")

    print(f"\nQuiz Finished! 🎊\nYour total score is: {score}/{len(questions)}")
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
