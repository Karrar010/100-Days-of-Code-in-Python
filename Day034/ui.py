from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20,pady=40, bg=THEME_COLOR)

        # Score Text
        self.score_txt = Label(text=f"Score: 0", bg= THEME_COLOR, fg= "white" , font=( 20))
        self.score_txt.grid(column=1,row=0)

        self.canvas = Canvas(bg="white", width=400,height=400)
        self.question_txt_canvas = self.canvas.create_text(
            200,200,  # x and y position of text
            text="Some Question", 
            width= 340,
            font=("Arial", 20, "italic"), fill= THEME_COLOR
        )
        self.canvas.grid(column=0,row=1,columnspan=2,pady=20)

        # Buttons
        true_img = PhotoImage(file="./Day34/images/true.png")
        false_img = PhotoImage(file="./Day34/images/false.png")

        self.correct_btn = Button(image=true_img, highlightthickness=0, command= self.true_pressed)
        self.correct_btn.grid(column=0,row=2)

        self.wrong_btn = Button(image=false_img, highlightthickness=0, command= self.false_pressed)
        self.wrong_btn.grid(column=1,row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_txt.config(text= f"Score: {self.quiz.score}")
            quiz_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_txt_canvas, text = quiz_question)
        else:
            self.canvas.itemconfig(self.question_txt_canvas, text = " QUIZ OVER ")
            self.correct_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")

    def true_pressed(self):
        self.your_guess = True
        self.check_guess(self.quiz.check_answer('True'))
        
    def false_pressed(self):
        self.your_guess = False
        is_guess_right = self.quiz.check_answer('False')
        self.check_guess(is_guess_right)

    def check_guess(self, is_guess_right):
        print(f"Correct Answer: {self.quiz.right_answer} , Your Answer: {self.your_guess}")
        if is_guess_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        #move to next question
        self.window.after(1000,self.get_next_question)

