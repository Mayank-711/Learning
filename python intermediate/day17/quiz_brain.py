class QuizBrain:
    def __init__(self,q_list):
        self.q_no = int(0)
        self.ques_list = q_list
        self.score = int(0)

    def stillhasques(self):
        if self.q_no < len(self.ques_list):
            return True
        else:
            return False
    def nextques(self):
        currentq = self.ques_list[self.q_no]
        a = input(f"Q.{self.q_no + 1}:{currentq.text} (True/False):")
        self.q_no += 1
        self.checkans(a,currentq.answer)
    def checkans(self,a,correct):
        if a == correct:
            self.score+=1
            print(f"Correct Your Score is {self.score}")
        else:
            print(f"Wrong Your Score is {self.score}")


