import tkinter as tk
from quiz_brain import QuizBrain
from tkinter import messagebox
import time

THEME_COLOR = "#375362"
LAYOUT_WIDTH = 800
LAYOUT_HEIGHT = 700


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = tk.Tk()
        self.window.title("Quizller")
        self.window.config(
            padx=20, pady=20, bg=THEME_COLOR, width=LAYOUT_WIDTH, height=LAYOUT_HEIGHT
        )
        self.question_canvas = tk.Canvas(
            width=LAYOUT_WIDTH / 2, height=LAYOUT_HEIGHT / 2, bg="white"
        )
        self.true_icon = tk.PhotoImage(file="./images/true.png")
        self.false_icon = tk.PhotoImage(file="./images/false.png")
        self.true_btn = tk.Button(
            image=self.true_icon,
            highlightthickness=0,
            command=lambda: self.check_answer("True"),
        )
        self.false_btn = tk.Button(
            image=self.false_icon,
            highlightthickness=0,
            command=lambda: self.check_answer("False"),
        )
        self.true_btn.image = self.true_icon
        self.false_btn.image = self.false_icon
        self.score = tk.Label(
            text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 20, "bold")
        )
        self.question_text = self.question_canvas.create_text(
            LAYOUT_WIDTH / 4,
            LAYOUT_HEIGHT / 4,
            text="Some Question Text",
            fill=THEME_COLOR,
            width=300,
        )
        self.__build_layout()
        self.get_next_question()
        self.window.mainloop()

    def __build_layout(self):

        self.score.grid(row=0, column=1)
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.true_btn.grid(row=2, column=0)
        self.false_btn.grid(row=2, column=1)

    def get_next_question(self):
        self.question_canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.question_canvas.itemconfig(self.question_text, text=q_text)

    def check_answer(self, user_answer: str):
        answer = self.quiz.check_answer(user_answer)

        if answer:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")

        if self.quiz.still_has_questions():
            self.window.after(1000, self.get_next_question)
        else:
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
            messagebox.showinfo(
                "Quiz Finished!",
                f"Your final score is {self.quiz.score}/{self.quiz.num_of_questions}",
            )
            self.window.destroy()
