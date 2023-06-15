import curses
from curses import wrapper
import Deck

def loadDeck(stdscr):
    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(0, 0, "loadDeck WIP")
    stdscr.addstr(1, 0, "Press enter to continue")
    stdscr.getch(2, 0)

def createDeck(stdscr):
    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(0, 0, "createDeck WIP")
    stdscr.addstr(1, 0, "Press enter to continue")
    stdscr.getch(2, 0)

def main(stdscr):
    curses.echo()
    stdscr.clear()
    stdscr.refresh()
    stdscr.keypad(True)
    stdscr.addstr(0, 0, "Welcome to the Flashcard Program!")
    running = True
    while running:
        stdscr.addstr(1, 0, "Please select an option by typing the corresponding number and then press enter:")
        stdscr.addstr(2, 4, "1. Load existing deck")
        stdscr.addstr(3, 4, "2. Create new deck")
        stdscr.addstr(4, 4, "3. Exit")
        userInput = None
        while userInput == None:
            userInput = stdscr.getch(5, 0)
            if userInput == ord('1'):
                loadDeck(stdscr)
            elif userInput == ord('2'):
                createDeck(stdscr)
            elif userInput == ord('3'):
                running = False
            else:
                stdscr.addstr(6, 0, "Invalid input. Please try again.")
                stdscr.delch(5, 0)
                userInput = None
                stdscr.refresh()
        stdscr.clear()
        stdscr.refresh()
    
if __name__ == '__main__':
    wrapper(main)