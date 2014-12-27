"""
TODO:
        DONE 1: disable god mode for selecting dice
        DONE 2: don't allow yahtzee to be scratched if yahtzeebonus hasn't been
        DONE 3: deal with yahtzeebonus if it has been used it cant be scratched 
        but need to be able to end the game.
        DONE 4: better handling of printing out the scorecard
        https://docs.python.org/2/tutorial/inputoutput.html
		DONE 5: don't have the window close after completion of the game
		DONE 6: investigate strange number trends.
"""
from calculations import *

def main():
    print(""" __      __            __          __                                   
|  \    /  \          |  \        |  \                                  
 \$$\  /  $$  ______  | $$____   _| $$_    ________   ______    ______  
  \$$\/  $$  |      \ | $$    \ |   $$ \  |        \ /      \  /      \ 
   \$$  $$    \$$$$$$\| $$$$$$$\ \$$$$$$   \$$$$$$$$|  $$$$$$\|  $$$$$$\ 
    \$$$$    /      $$| $$  | $$  | $$ __   /    $$ | $$    $$| $$    $$
    | $$    |  $$$$$$$| $$  | $$  | $$|  \ /  $$$$_ | $$$$$$$$| $$$$$$$$
    | $$     \$$    $$| $$  | $$   \$$  $$|  $$    \ \$$     \ \$$      
     \$$      \$$$$$$$ \$$   \$$    \$$$$  \$$$$$$$$  \$$$$$$$  \$$$$$$$
    """)
    
    
    choice = "y"
    while choice != "n":
        options = ["ones", "twos", "threes", "fours", "fives", "sixes", "tofakind", "fofakind", 
                   "fullhouse", "smlstraight", "lrgstraight", "yahtzee", "chance", "yahtzeebonus"]
        staticoptions = ["ones", "twos", "threes", "fours", "fives", "sixes", "tofakind", "fofakind", 
                   "fullhouse", "smlstraight", "lrgstraight", "yahtzee", "chance", "yahtzeebonus"]
        scorecard = ['','','','','','','','','','','','','','']
        finalscore = 0
        end = ['','','','','','','','','','','','','','']
        
        while options != end:
            dice.turn(options, scorecard)
            print("\nHere is your current score card: ")
            tmpsc = ['','','','','','','','','','','','','','']
            for x in range(0,14):
                if scorecard[x] == '':
                    tmpsc[x] = "none yet"
                else:
                    tmpsc[x] = scorecard[x]
            
            for x in range(0,14):            
                print('{0:12} | {1}'.format(staticoptions[x], tmpsc[x]))
            print("")
            
        if sum(scorecard[0:6]) > 62:
            finalscore = 35
            print("Your final score for the numbers is over 62 so you received a bonus 35 points.")
            
        finalscore += sum(scorecard)
        
        print("Your final score was " + str(finalscore))
        choice = input("Would you like to play a round of Yahtzee? y or n: ")
main()