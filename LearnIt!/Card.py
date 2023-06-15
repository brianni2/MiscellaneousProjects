class Card:
    def __init__(self):
        self.question = ""
        self.choices = []
        self.answer = ""
        self.accuracy = 0
        
    def createCard(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer
        return True
        
    def getQuestion(self):
        return self.question
    
    def getChoices(self):
        return self.choices
    
    def checkAnswer(self, answer):
        if answer == self.answer:
            if self.accuracy < 100:
                self.accuracy += 35
            return True
        else:
            if self.accuracy >= 10:
                self.accuracy -= 10
            else:
                self.accuracy = 0
            return False