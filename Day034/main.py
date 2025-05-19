#1. ADD QUIZZLER DATABASE API 
#2. RESOLVE THE HTML ENTITIES THAT POP UP IN THE QUESTION TEXT
#3. ADD GUI TO THE QUIZ GAME
#4. ADD WORKING OF BUTTONS
#5. WHEN QUESTIONS ARE FINISHED

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():  #cannot run a while loop since mainloop is running
#     quiz.next_question()