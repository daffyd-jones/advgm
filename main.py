from state import State
import os
import sys
def main():
    # p = Player()
    play = True
    scene = None
    if len(sys.argv) > 1:
        scene = sys.argv[1]

    while play:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Welcome to VALLEY QUEST!!!")
        print("KEYWORDS displayed in CAPS are used to make decisions, \
            \nthe responses can be lowercase or caps. \n\
            \nAt any point other than an encounter, 'menu' and 'inv' can\
            \nbe used to access the menu or player inventory\n\
            \npress Enter to advance")
        print("")
        play = str(input(""))
        print("would you like to play? Y/N")
        play = str(input(": ")).upper()
        if play == "Y":
            state = State()
            state.play(scene)
        else:
            print("Ok bye")
            break




main()
