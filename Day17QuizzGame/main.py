from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_question = Question(question['text'], question['answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
final_score = 0
number_of_questions = 0

while (quiz.still_has_questions()):
    quiz.next_question()

print(f"You completed the quiz, your final score is {quiz.score}/{quiz.question_number}")
