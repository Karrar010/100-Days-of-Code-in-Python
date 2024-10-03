from data import question_data
from question_model import Question
from quiz_brain import Quizbrain

question_bank = []
for x in range(0,len(question_data)):
    new_question = Question(question_data[x]["text"],question_data[x]["answer"])
    question_bank.append(new_question)

# print(question_bank[1].q_text)
quiz = Quizbrain(question_bank)

print("\n----------------------------------------------------------------------")
print("\t\t\tDIGITAL QUIZ")
print("----------------------------------------------------------------------\n")
while quiz.question_remain():
    quiz.next_question()

print("You have Completed the Quiz")
print(f"Congratulations you scored {quiz.score}/{len(question_bank)}")