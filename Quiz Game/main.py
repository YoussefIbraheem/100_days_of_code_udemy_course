from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
questions_bank = []

for question in question_data:
    new_question = Question(question['question'],question['correct_answer'])
    questions_bank.append(new_question)

quiz = QuizBrain(questions_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")

print(f"Final Score {quiz.score}/{quiz.question_number}")