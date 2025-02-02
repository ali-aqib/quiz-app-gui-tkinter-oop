import html


# Defining class
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    # method to check the remaining questions
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # method for generating next question
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1

        # un-escaping HTML special characters like &quot etc
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    # method for checking answer
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False
