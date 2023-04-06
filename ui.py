from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Creating the widgets
        self.score = 0
        self.Score = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="White", font=("Arial", 15, "bold"))
        self.canvas = Canvas(width=400, height=350, bg="White")
        self.question_text = self.canvas.create_text(200, 175, text="Press any Button.", width=380,
                                                     font=("Arial", 20, "italic"))
        img1 = PhotoImage(file='images/true.png')
        img2 = PhotoImage(file='images/false.png')
        self.right = Button(image=img1, bg=THEME_COLOR, highlightthickness=0, command=self.from_right)
        self.wrong = Button(image=img2, bg=THEME_COLOR, highlightthickness=0, command=self.from_wrong)
        # Placing the widgets on the screen
        self.Score.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.right.grid(row=2, column=0)
        self.wrong.grid(row=2, column=1)
        # Calling the questions
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            self.Score.config(text=f"Score: {self.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Quiz Completed")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")

    def from_right(self):
        self.printing_result(self.quiz.check_answer("True"))

    def from_wrong(self):
        self.printing_result(self.quiz.check_answer("False"))

    def printing_result(self, ans: str):
        if ans == "Right":
            s = "Green"
            self.score += 1
        else:
            s = "Red"
        self.canvas.config(bg=s)
        self.window.after(1000, self.get_next_question)
