from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.title("Quizzler")

        self.canvas = Canvas(self.window, height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Some Question Text",
                                                     fill=THEME_COLOR,
                                                     font=("Ariel", 20, "italic"), anchor="center")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(self.window, text=f"Score: 0", bg=THEME_COLOR, fg="white", font=("Ariel", 20))
        self.score_label.grid(row=0, column=1)

        image_true = PhotoImage(file="C:/Users/infoa/PycharmProjects/day-33 quizzler-app-start/images/true.png")
        image_false = PhotoImage(file="C:/Users/infoa/PycharmProjects/day-33 quizzler-app-start/images/false.png")
        self.button_true = Button(self.window, image=image_true, bg=THEME_COLOR,
                                  fg=THEME_COLOR, highlightthickness=0, relief="flat", command=self.true_pressed)
        self.button_true.grid(row=2, column=0, padx=10, pady=10)
        self.button_false = Button(self.window, image=image_false, bg=THEME_COLOR,
                                   fg=THEME_COLOR, highlightthickness=0, relief="flat", command=self.false_pressed)
        self.button_false.grid(row=2, column=1, padx=10, pady=10)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")

        self.window.after(1000, self.get_next_question)
