# termux_quiz.py

print("\033[92mWelcome to Termux Quiz!\033[0m")

score = 0

questions = [
    {"question": "\033[92mQ1: What command is used to enter any folder?\033[0m", "answer": "cd"},
    {"question": "\033[92mQ2: What command is used to check folder?\033[0m", "answer": "ls"},
    {"question": "\033[92mQ3: What is Termux back command?\033[0m", "answer": "exit"},
    {"question": "\033[92mQ4: What is the command to install Python in Termux?\033[0m", "answer": "pkg install python"},
    {"question": "\033[92mQ5: What command is used to install color module?\033[0m", "answer": "pip install color"},
    {"question": "\033[92mQ6: What is the pkg name used to create files in Termux?\033[0m", "answer": "nano"}
]

for question in questions:
    user_answer = input(question["question"] + " ")
    if user_answer.lower() == question["answer"].lower():
        print("\033[92mYour Answer is Right!\033[0m")
        score += 10
    else:
        print("\033[91mWrong input!\033[0m")

print(f"\nYour Score: {score}/60")

if score == 60:
    print("\033[92mCongratulations! You Win! You will add in Next Test.\033[0m")