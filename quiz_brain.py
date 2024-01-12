class QuizBrain:
        def __init__(self, q_list) -> None:
                self.question_list = q_list
                self.question_number = 0
                self.skore = 0
        
        def next_question(self):
                current_question = self.question_list[self.question_number]
                self.question_number+=1
                user_answer = input(f"Otázka číslo {self.question_number}: {current_question.text} (True/False): ")
                self.check_answer(current_question.answer, user_answer)

        def check_answer(self,answer,user_answer):
                if answer.lower()==user_answer.lower():
                    print ("Spravne")
                    self.skore+=1
                else:
                    print("Spatne!")

        def has_questions(self):
                if self.question_number<len(self.question_list):
                    return True
                else:
                    return False
                
       