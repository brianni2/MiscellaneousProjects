class Card:
    def __init__(self, question="", choices=[], answer=[], accuracy=0):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.accuracy = accuracy

    def getQuestion(self):
        return self.question
    
    def getChoices(self):
        return self.choices
    
    def getAnswer(self):
        return self.answer
    
    def checkAnswer(self, answer):
        total_correct = 0
        for i in range(len(answer)):
            if answer[i] == self.answer[i]:
                total_correct += 1
        if total_correct == len(answer):
            if self.accuracy > 65:
                self.accuracy = 100
            else:
                self.accuracy += 35
            return 2
        elif total_correct == 0:
            if self.accuracy < 10:
                self.accuracy = 0
            else:
                self.accuracy -= 10
            return 1
        else:
            if self.accuracy > 90:
                self.accuracy = 100
            else:
                self.accuracy += 10
            return 0