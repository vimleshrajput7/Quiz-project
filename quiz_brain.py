class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list = q_list
        self.score=0
        #self.current_question.answer
        #print(current_question.answer)

#if still question bank has questions than rtuern True
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

#print next question and increase question number
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"Q.{self.question_number}:{current_question.text} (True/False): ")
        self.check_answer(user_answer,current_question.answere)
        ##check_answer_positional arg(user_answer=user_answer,current_question.answere=correct_answer)   

#check answere from question_bank & and print score
    def check_answer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score +=1
            print("you got right answer")
        else:
            print("thats wrong answer")
            print(f"the correct answer was {correct_answer}. ")
            print(f"your current score is {self.score}/{self.question_number} ")
            print("\n")


    