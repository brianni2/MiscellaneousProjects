import os
import curses
import random
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
    stdscr.clear()
    stdscr.refresh()
    return deck

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
    stdscr.clear()
    stdscr.refresh()
    return deck

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
                else:
                    studyDeck(stdscr, deck)
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
        stdscr.addstr(1,0, f"Card {index + 1} of {deck.getCardCount()}")
        stdscr.addstr(2,0, deck.getCard(index).getQuestion())
        choices = deck.getCard(index).getChoices()
        for i in range(len(choices)):
            stdscr.addstr(4 + (2*i), 4, f"({choices[i][0]}) {choices[i][1]}")
        stdscr.addstr(4 + (2*len(choices)), 0, f"Answer: {deck.getCard(index).getAnswer()}")
        userInput = None
        while userInput == None:
            userInput = chr(stdscr.getch(0, 77))
            if userInput == 'a':
                if index > 0:
                    index -= 1
                else:
                    index = deck.getCardCount() - 1
            elif userInput == 'd':
                if index < deck.getCardCount() - 1:
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
        choices_str = stdscr.getstr(5, 0).decode('utf-8')
        if len(choices_str) == 0:
            stdscr.deleteln()
            stdscr.addstr(4, 0, "Please enter a valid choice.")
            choices_str = None
            stdscr.refresh()
        else:
            break
    while answer == None:
        stdscr.addstr(6, 0, "Please enter the number to the correct answer(s) in the order which you entered the choices, seperated by commas:")
        answer_str = stdscr.getstr(8, 0).decode('utf-8')
        if len(answer_str) == 0:
            stdscr.deleteln()
            stdscr.addstr(7, 0, "Please enter a valid answer.")
            answer_str = None
            stdscr.refresh()
        else:
            break
    choices_str = choices_str.split('\#')
    choices = []
    for i in range(len(choices_str)):
        choices.append((i+1, choices_str[i]))
    answer = list(map(str, answer_str.split(',')))
    card = Card(question, choices, answer)
    return card

def studyDeck(stdscr, deck):
    stdscr.clear()
    stdscr.refresh()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    incorrect_text = curses.color_pair(1)
    correct_text = curses.color_pair(2)
    study_list = []
    study_order = list(range(deck.getCardCount()))
    random.shuffle(study_order)
    for i in study_order:
        study_list.append(deck.getCard(i))
    curr_list = []
    running = True
    userInput = None
    while running:
        if len(study_list) < 11:
            curr_list = study_list.copy()
        else:
            curr_list = study_list[0:10]
        total_correct = 0
        for index in range(len(curr_list)):
            stdscr.addstr(0,0, f"Question {index + 1} of {len(curr_list)}")
            stdscr.addstr(2,0, curr_list[index].getQuestion())
            choices = random.sample(curr_list[index].getChoices(), len(curr_list[index].getChoices()))
            for i in range(len(choices)):
                stdscr.addstr(4 + (2*i), 4, f"({i+1}) {choices[i][1]}")
            userInput = None
            while userInput == None:
                stdscr.addstr(1, 0, "Please enter your answer seperated by commas (if applicable):")
                userInput = stdscr.getstr(1, 63).decode('utf-8')
                user_answers = userInput.split(',')
                if len(user_answers) == 0 or len(user_answers) > len(choices):
                    stdscr.deleteln()
                    stdscr.addstr(2, 0, "Please enter a valid answer.")
                    userInput = None
                    stdscr.refresh()
                else:
                    matched_answer = []
                    for i in range(len(user_answers)):
                        matched_answer.append(choices[int(user_answers[i])-1][0])
                    if curr_list[index].checkAnswer(matched_answer) == 2:
                        total_correct += 1
                        study_list.remove(curr_list[index])
                    for i in range(len(choices)):
                        if choices[i][0] in curr_list[index].getAnswer():
                            stdscr.addstr(4 + (2*i), 4, f"({i+1}) {choices[i][1]}", correct_text)
                        else:
                            stdscr.addstr(4 + (2*i), 4, f"({i+1}) {choices[i][1]}", incorrect_text)
                stdscr.addch(1,0, ' ')
                stdscr.deleteln()
                stdscr.addstr(1, 0, "Press any key to continue.")
                stdscr.getch(1, 27)
            stdscr.clear()
            stdscr.refresh()
        stdscr.addstr(0, 0, f"You got {total_correct} out of {len(curr_list)} correct!")
        stdscr.addstr(1, 0, "Would you like to continue studying?")
        stdscr.addstr(2, 0, "1. Yes")
        stdscr.addstr(3, 0, "2. No (Return to deck menu)")
        userInput = None
        while userInput == None:
            userInput = chr(stdscr.getch(5,0))
            if userInput == '1':
                break
            elif userInput == '2':
                running = False
                break
            else:
                stdscr.deleteln()
                userInput = None
                stdscr.refresh()
        stdscr.clear()
        stdscr.refresh()

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
                deck = loadDeck(stdscr)
                deckMenu(stdscr, deck)
                continue
            elif userInput == '2':
                deck = createDeck(stdscr)
                deckMenu(stdscr, deck)
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