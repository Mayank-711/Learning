from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
qb = []
for value in question_data:
    ques = value["text"]
    ans = value["answer"]
    new_q = Question(ques,ans)
    qb.append(new_q)
Q1 = QuizBrain(qb)
while Q1.stillhasques() == True:
     Q1.nextques()

