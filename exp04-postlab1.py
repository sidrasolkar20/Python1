'''Exp(Postlab01)
Aim:Write a program in Python that generates a quiz and uses two files– Question.txt and Answers.txt. The program open Question.txt and read a question and displays the
question with option on the screen. The program then opens the Answers.txt file'''
# Name: Sidra Solkar
# UIN:231P087
# Roll No.:43
# Function to read questions from Question.txt
def load_questions(filename):
    with open(filename, 'r') as file:
        questions = file.read().strip().split("\n\n")  
    return questions

def load_answers(filename):
    with open(filename, 'r') as file:
        answers = [line.strip() for line in file.readlines()]
    return answers

def ask_question(question, options):
    print(question)  
    for option in options:  
        print(option)
   
    answer = input("Your answer (a, b, c, d): ").strip().lower()
    return answer

def run_quiz():
    questions = load_questions('Question.txt')  
    answers = load_answers('Answers.txt')  
    
    score = 0  
    total_questions = len(questions)
    
    for i, question_block in enumerate(questions):
        question_lines = question_block.split("\n")
        question = question_lines[0]  
        options = question_lines[1:]  
        
        user_answer = ask_question(question, options)
       
        if user_answer == answers[i]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {answers[i]}.")

        print()

    print(f"Quiz Over! Your score: {score}/{total_questions}")
    print("\nName: Sidra Solkar \nUIN:231P087 \nRoll no:43")

if __name__ == "__main__":
    run_quiz()
