from tkinter import *
from quiz_brain import *


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.minsize(width=340, height=600)
        self.window.maxsize(width=340, height=600)

        self.canvas = Canvas(bg="white", height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, fill="black", font="Arial 15 italic",
                                text="Quiz game on", width=280, justify="center")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.lbl_score = Label(text=f"Score:{self.quiz.score}", bg=THEME_COLOR, fg="white", highlightthickness=0)
        self.lbl_score.grid(column=1, row=0)

        true_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.select_true)
        false_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.select_false)
        self.true_btn.grid(column=0, row=2, padx=20, pady=20)
        self.false_btn.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.lbl_score.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="GAME OVER: you've reached the end of the quiz!")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def select_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def select_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)
