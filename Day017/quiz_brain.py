class Quizbrain:
    def __init__(self,q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0
    def question_remain(self):
        return self.question_num < len(self.question_list)
    
    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num}: {current_question.q_text} (True/False)  Ans: ")
        self.check_answer(user_answer,current_question.q_answer)

    def check_answer(self,user_ans,correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("You are Right")
        else:
            print("You are Wrong")
        print(f"The correct answer was: {correct_ans}")
        print(f"Current Score is {self.score}/{self.question_num}\n")