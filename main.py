#-----------------------------------------------------Question_quiz_project--------------------------------------------------------------------#

from data import question_data 
from question_model import question 
from quiz_brain import QuizBrain


#make a question_bank fron question_data file 
question_bank=[]
for que in question_data:
    question_text= que["text"]
    question_answer=que["answer"]
    new_question = question(question_text,question_answer) #call class question(q_text,q_answere)
    question_bank.append(new_question)
    print(question_bank[0].answere)


#call class_functions
quiz= QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

#when we complete the quize print alert and show score
print("you have complete the quiz")
print(f"your final score {quiz.score}/{quiz.question_number}")