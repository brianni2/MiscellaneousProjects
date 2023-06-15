import Card
import json

class Deck:
    def __init__(self):
        self.cards = []
        
    def addCard(self, card):
        self.cards.append(card)
        return True
    
    def createCard(self, question, choices, answer):
        card = Card.Card()
        card.createCard(question, choices, answer)
        self.cards.append(card)
        return True
    
    def getCards(self):
        return self.cards
    
    def getCard(self, index):
        return self.cards[index]
    
    def saveDeck(self, filename):
        with open(filename, 'w') as outfile:
            json.dump(self, outfile, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        return True
    
    def loadDeck(self, filename):
        with open(filename) as infile:
            data = json.load(infile)
        self.cards = data['cards']
        return True