from tkinter import *
from quiz_brain import QuizBrain
import os
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):  # Accessing QuizBrain class and defining the data type for readability
        # object of QuizBrain class from quiz_brain.py
        self.quiz = quiz_brain

        # Creating tkinter window
        self.window = Tk()
        # setting background color and padding
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        # title of the window
        self.window.title("Quizzler")

        # creating canvas in tkinter window
        self.canvas = Canvas(self.window, height=250, width=300, bg="white")
        # Creating text in canvas
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Some Question Text",
                                                     fill=THEME_COLOR,
                                                     font=("Ariel", 20, "italic"), anchor="center")
        # placing canvas in window
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # creating score label
        self.score_label = Label(self.window, text=f"Score: 0", bg=THEME_COLOR, fg="white", font=("Ariel", 20))
        self.score_label.grid(row=0, column=1)

        # reading images for buttons
        script_dir = os.path.dirname(__file__)
        image_true = PhotoImage(file=os.path.join(script_dir, 'images', 'true.png'))
        image_false = PhotoImage(file=os.path.join(script_dir, 'images', 'false.png'))

        # creating "Right" and "Wrong" buttons
        self.button_true = Button(self.window, image=image_true, bg=THEME_COLOR,
                                  fg=THEME_COLOR, highlightthickness=0, relief="flat", command=self.true_pressed)
        self.button_true.grid(row=2, column=0, padx=10, pady=10)
        self.button_false = Button(self.window, image=image_false, bg=THEME_COLOR,
                                   fg=THEME_COLOR, highlightthickness=0, relief="flat", command=self.false_pressed)
        self.button_false.grid(row=2, column=1, padx=10, pady=10)

        # Calling get_next_question() method
        self.get_next_question()

        # close the window on click the ❌
        self.window.mainloop()

    # Place the next question on the canvas
    def get_next_question(self):
        # update score label
        self.score_label.config(text=f"Score: {self.quiz.score}")
        # change the canvas color back to white
        self.canvas.config(bg="white")
        # calling still_has_question method from class QuizBrain
        if self.quiz.still_has_questions():
            # getting question text using next_question method from QuizBrain class
            q_text = self.quiz.next_question()
            # placing question on canvas
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # showing final score when questions end and disabling the buttons
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz.\nYour final score is "
                                                            f"{self.quiz.score}/15")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    # function bound to ✅ button
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    # function bound to ❌ button
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    # method change the color of canvas to green or red  based on the answer and execute the get_next_question method
    # after 1 second
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")

        self.window.after(1000, self.get_next_question)
