from re import T
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(question['text'], question['answer']) for question in question_data]

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(quiz.final_score())