import html     
# The question text when printed shows entity names or entity numbers to instead of symbol like , . <  > etc
# this is because in html when add these symbols the website interprets them as code which causes issues, to avoid this we use html library 
# properties like escape, unescape; escape is for conveting simple text in html entity format and unescape convert the entities into symbold
# Like:
# Entity Name: #quote? -->> "  (symbols) 
# Entity Number: &#60 -->>  <

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        self.right_answer = 0  # since varible is only created to print correct answer in terminal

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        quest_txt = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {quest_txt}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        self.right_answer = correct_answer
        # print(correct_answer)
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            # print("You got it right!")
            return True
        else:
            # print("That's wrong.")
            return False