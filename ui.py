from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, width=600, height=900)

        self.label = Label()
        self.label.config(text="Score: 0", bg=THEME_COLOR, fg="white",
                          font=("courier", 20, "normal"))
        self.label.grid(column=1, row=0, pady=20)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.config(bg="white")
        self.question = self.canvas.create_text(150, 100, text="Question Here",
                                                font=("arial", 20, "italic"),
                                                fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        right_img = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=right_img, highlightthickness=0,
                                   borderwidth=0, command=self.right_button)
        self.right_button.grid(column=0, row=2, pady=20)

        wrong_img = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=wrong_img, highlightthickness=0,
                                   borderwidth=0, command=self.wrong_button)
        self.wrong_button.grid(column=1, row=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        # self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=q_text)

    def right_button(self):
        answer = self.quiz.check_answer("True", self.quiz.question_list[self.quiz.question_no].answer)
        self.give_feedback(answer)

    def wrong_button(self):
        answer = self.quiz.check_answer("False", self.quiz.question_list[self.quiz.question_no].answer)
        self.give_feedback(answer)

    def give_feedback(self, answer):
        print(answer)
        if answer:
            self.canvas.config(bg="green")
            self.label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(0, self.get_next_question())
