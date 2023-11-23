import random


def generate_question():
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    operator = random.choice(['+', '-', '*', '/'])
    question = f"What is {num1} {operator} {num2}?"
    return question, eval(f'{num1} {operator} {num2}')


def main():
    correct_answers = 0
    total_questions = 4

    for _ in range(total_questions):
        question, correct_answer = generate_question()
        user_answer = float(input(question + ''))

        if round(user_answer, 1) == round(correct_answer, 1):
            print(f'{question} {user_answer}\nYour answer is correct!\n')
            correct_answers += 1
        else:
            print(f'{question} {user_answer}\nYour answer is incorrect. The correct answer is {correct_answer}\n')

    print(f'You answered {correct_answers} out of {total_questions} questions correctly.')


if __name__ == "__main__":
    main()
