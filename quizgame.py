#python quiz game

questions = (
    "What is the capital of France?",
    "What is the largest planet in our solar system?",
    "What is the chemical symbol for gold?",
    "What is the powerhouse of the cell?",
    "what is the largest ocean on Earth?"
)

options = (
    ("A. Paris", "B. London", "C. Berlin", "D. Madrid"),
    ("A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"),
    ("A. Au", "B. Ag", "C. Fe", "D. Hg"),
    ("A. Nucleus", "B. Mitochondria", "C. Ribosome", "D. Endoplasmic Reticulum"),
    ("A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean")
)

answers = ("A", "B", "A", "B", "D")
guesses = []
score = 0
question_num = 0

for every_question in questions:
    print("-------------------------")
    print(every_question)
    for option in options[question_num]:
        print(option)
guess = input("Enter (A, B, C, or D): ").upper()
guesses.append(guess)

if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
else:
        print("WRONG!")
        print(f"{answers[question_num]} is the correct answer.")
    
question_num += 1