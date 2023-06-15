import os
import curses
from curses import wrapper
from Card import Card
from Deck import Deck

def loadDeck(stdscr):
    stdscr.clear()
    stdscr.refresh()
    fileName = None
    while fileName == None:
        stdscr.addstr(0, 0, "Please enter the name of the deck you want to load:")
        fileName = stdscr.getstr(2, 0)
        if len(fileName) == 0:
            stdscr.deleteln()
            stdscr.addstr(1, 0, "Please enter a valid name.")
            fileName = None
            continue
        else:
            fileName = os.path.join(os.getcwd(), 'data', fileName.decode('utf-8') + '.json')
            break
    deck = Deck()
    try: 
        deck.loadDeck(fileName)
        stdscr.addstr(3, 0, f"Deck {deck.name} loaded successfully!")
        stdscr.addstr(4, 0, "Press enter to continue")
        stdscr.getch(5, 0)
    except:
        stdscr.addstr(3, 0, f"Deck {fileName} not found.")
        stdscr.addstr(4, 0, "Press enter to continue")
        stdscr.getch(5, 0)
    deckMenu(stdscr, deck)
    stdscr.clear()

def createDeck(stdscr):
    stdscr.clear()
    stdscr.refresh()
    userInput = None
    while userInput == None:
        stdscr.addstr(0, 0, "Please enter the name of your new deck:")
        userInput = stdscr.getstr(2, 0)
        if len(userInput) == 0:
            stdscr.deleteln()
            stdscr.addstr(1, 0, "Please enter a valid name.")
            userInput = None
            continue
        else:
            userInput = userInput.decode('utf-8')
            break
    deck = Deck(userInput)
    stdscr.addstr(3, 0, f"Deck {deck.name} created successfully!")
    stdscr.addstr(4, 0, "Press enter to continue")
    stdscr.getch(5, 0)
    deckMenu(stdscr, deck)

def deckMenu(stdscr, deck):
    stdscr.clear()
    stdscr.refresh()
    running = True
    userInput = None
    while running:
        stdscr.addstr(0, 0, f"Deck: {deck.name}")
        stdscr.addstr(1, 0, "Please select an option by typing the corresponding number and then press enter:")
        stdscr.addstr(2, 4, "1. View deck")
        stdscr.addstr(3, 4, "2. Add card")
        stdscr.addstr(4, 4, "3. Study deck")
        stdscr.addstr(5, 4, "4. Save deck")
        stdscr.addstr(6, 4, "5. Exit")
        userInput = None
        while userInput == None:
            userInput = chr(stdscr.getch(8, 0))
            if userInput == '1':
                if len(deck.cards) == 0:
                    stdscr.deleteln()
                    stdscr.addstr(7, 0, "There are no cards in this deck to view")
                    userInput = None
                    stdscr.refresh()
                else:
                    viewDeck(stdscr, deck)
                continue
            elif userInput == '2':
                new_card = newCard(stdscr)
                deck.addCard(new_card)
                continue
            elif userInput == '3':
                if len(deck.cards) == 0:
                    stdscr.deleteln()
                    stdscr.addstr(7, 0, "There are no cards in this deck to study")
                    userInput = None
                    stdscr.refresh()
                continue
            elif userInput == '4':
                fileName = os.path.join(os.getcwd(), 'data', deck.name + '.json')
                deck.saveDeck(fileName)
                continue
            elif userInput == '5':
                running = False
                break
            else:
                stdscr.deleteln()
                userInput = None
                stdscr.refresh()
        stdscr.clear()
        stdscr.refresh()

def viewDeck(stdscr, deck):
    stdscr.clear()
    stdscr.refresh()
    running = True
    userInput = None
    index = 0
    while running:
        stdscr.addstr(0,0, "Press a to go to the previous card, d to go to the next card, or q to quit:")
        stdscr.addstr(1,0, f"Card {index + 1} of {len(deck.cards)}")
        stdscr.addstr(2,0, deck.getCard(index).getQuestion())
        choices = deck.getCard(index).getChoices()
        for i in range(len(choices)):
            stdscr.addstr(4 + (2*i), 4, f"({choices[i][0]}) {choices[i][1]}")
        userInput = None
        while userInput == None:
            userInput = chr(stdscr.getch(0, 77))
            if userInput == 'a':
                if index > 0:
                    index -= 1
                else:
                    index = len(deck.cards) - 1
            elif userInput == 'd':
                if index < len(deck.cards) - 1:
                    index += 1
                else:
                    index = 0
            elif userInput == 'q':
                running = False
                break
            else:
                stdscr.delch(0, 77)
                userInput = None
                stdscr.refresh()
        stdscr.clear()
        stdscr.refresh()

def newCard(stdscr):
    stdscr.clear()
    stdscr.refresh()
    question = None
    choices_str = None
    answer = None
    while question == None:
        stdscr.addstr(0, 0, "Please enter your question:")
        question = stdscr.getstr(2, 0)
        if len(question) == 0:
            stdscr.deleteln()
            stdscr.addstr(1, 0, "Please enter a valid question.")
            question = None
            stdscr.refresh()
        else:
            question = question.decode('utf-8')
            break
    while choices_str == None:
        stdscr.addstr(3, 0, "Please enter your choices separated by \#:")
        choices_str = stdscr.getstr(5, 0)
        if len(choices_str) == 0:
            stdscr.deleteln()
            stdscr.addstr(4, 0, "Please enter a valid choice.")
            choices_str = None
            stdscr.refresh()
        else:
            choices_str = choices_str.decode('utf-8')
            break
    while answer == None:
        stdscr.addstr(6, 0, "Please enter the letter to correct answer in the order which you entered the choices:")
        answer = chr(stdscr.getch(8, 0))
        if len(answer) == 0:
            stdscr.deleteln()
            stdscr.addstr(7, 0, "Please enter a valid answer.")
            answer = None
            stdscr.refresh()
        else:
            break
    choices_str = choices_str.split('\#')
    choices = []
    for i in range(len(choices_str)):
        choices.append((chr(65+i), choices_str[i]))
    card = Card(question, choices, answer)
    return card

def main(stdscr):
    curses.echo()
    curses.nocbreak()
    curses.curs_set(2)
    stdscr.clear()
    stdscr.refresh()
    stdscr.keypad(True)
    stdscr.addstr(0, 0, "Welcome to LearnIt!")
    running = True
    while running:
        stdscr.addstr(1, 0, "Please select an option by typing the corresponding number and then press enter:")
        stdscr.addstr(2, 4, "1. Load existing deck")
        stdscr.addstr(3, 4, "2. Create new deck")
        stdscr.addstr(4, 4, "3. Exit")
        userInput = None
        while userInput == None:
            userInput = chr(stdscr.getch(6, 0))
            if userInput == '1':
                loadDeck(stdscr)
                continue
            elif userInput == '2':
                createDeck(stdscr)
                continue
            elif userInput == '3':
                running = False
                break
            else:
                stdscr.deleteln()
                userInput = None
                stdscr.refresh()
        stdscr.clear()
        stdscr.refresh()
    
if __name__ == '__main__':
    if not os.path.exists(os.path.join(os.getcwd(), 'data')):
        os.makedirs(os.path.join(os.getcwd(), 'data'))
    wrapper(main)
    print("Thank you for using LearnIt!")