def runQuiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        while True:
            resp = str(input("Choose your answer: ")).strip().upper()
            if resp not in "ABCD":
                print("Escolha apenas uma das opções!")
                continue
            else:
                if resp == question["answer"]:
                    score += 1
                    print("Correct answer!")
                    break
                else:
                    print(f"Wrong answer! The correct one was {question['answer']}")
                    break
    print(f"Voce acertou {score} questoes e conseguiu uma pontuação de {score * 10}")

questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "prompt": "Which language is primarily spoken in Brazil?",
        "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "answer": "B"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "A"
    }
]

runQuiz(questions)