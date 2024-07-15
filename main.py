from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Creating list of objects from class Question that contains only question text and answer from data.py
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# creating quiz object from QuizBrain class and passing the question bank list.
quiz = QuizBrain(question_bank)

# creating quiz_ui object from QuizInterface class and passing the quiz object into it.
quiz_ui = QuizInterface(quiz)

