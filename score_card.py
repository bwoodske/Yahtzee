'''
Ones x amt
twos x amt
threes x amt
fours x amt
fives x amt
sixes x amt
bonus 35 pts if score is 63 <=

3 of a kind:    ttl of all dice
4 of a kind:    ttl of all dice
full house:     25 pts
small stright   30 pts
large straight  40 pts
yahtzee         50 pts
chance          ttl of all dice
yahtzee bonus   100 each
'''
import os

class score_card:    
    def selection(dice, options, score):
        print("\nYou may either select one to score as or choose one to scratch")
        i=0
        while i == 0:
            if score == ['','','','','','','','','','','','','','']:
                print("\nHere are your options:")
                staticoptions = ["ones", "twos", "threes", "fours", "fives", "sixes", "tofakind", "fofakind",
                    "fullhouse", "smlstraight", "lrgstraight", "yahtzee", "chance", "yahtzeebonus", "scratch"]
                propnames = ["Count of #1 dice", "Count of #2 dice", "Count of #3 dice", "Count of #4 dice",
                             "Count of #5 dice", "Count of #6 dice", "Three of a kind", "Four of a kind",
                             "Full house", "Small straight", "Large straight", "Yahtzee", "Chance",
                             "Yahtzee bonus", "Select a row to scratch"]
                for x in range(0,15):
                    print('{0:12} = {1}'.format(staticoptions[x], propnames[x]))
                print("")
                print(dice)
            choice = input("Please enter the name of your choice or h for help: ")
            os.system('cls')
            if choice in options or choice == 'h':
                if choice == "ones":
                    if dice.count(1) > 0:
                        score[0] = dice.count(1)
                        print("You have claimed your ones column and your score for it is: " + str(score[0]))
                        options[0] = ""
                        i = 1
                elif choice == "twos":
                    if dice.count(2) > 0:
                        score[1] = dice.count(2)*2
                        print("You have claimed your twos column and your score for it is: " + str(score[1]))
                        options[1] = ""
                        i = 1
                elif choice == "threes":
                    if dice.count(3) > 0:
                        score[2] = dice.count(3)*3
                        print("You have claimed your threes column and your score for it is: " + str(score[2]))
                        options[2] = ""
                        i = 1
                elif choice == "fours":
                    if dice.count(4) > 0:
                        score[3] = dice.count(4)*4
                        print("You have claimed your fours column and your score for it is: " + str(score[3]))
                        options[3] = ""
                        i = 1
                elif choice == "fives":
                    if dice.count(5) > 0:
                        score[4] = dice.count(5)*5
                        print("You have claimed your fives column and your score for it is: " + str(score[4]))
                        options[4] = ""
                        i = 1
                elif choice == "sixes":
                    if dice.count(6) > 0:
                        score[5] = dice.count(6)*6
                        print("You have claimed your sixes column and your score for it is: " + str(score[5]))
                        options[5] = ""
                        i = 1
                elif choice == "tofakind":
                    if [i for i in dice if dice.count(i) > 2]:
                        score[6] = sum(dice)
                        print("You have claimed your three of a kind column with a score of: " + str(score[6]))
                        options[6] = ""
                        i = 1
                    else:
                        print("You do not have three dice of any one number")
                elif choice == "fofakind":
                    if [i for i in dice if dice.count(i) > 3]:
                        score[7] = sum(dice)
                        print("You have claimed your four of a kind column with a score of: " + str(score[7]))
                        options[7] = ""
                        i = 1
                    else:
                        print("You do not have four dice of any one number")
                elif choice == "fullhouse":
                    if [i for i in dice if dice.count(i) == 3] and [i for i in dice if dice.count(i) == 2]:
                        score[8] = 25
                        print("You have claimed your full house and have gained 25 points.")
                        options[8] = ""
                        i = 1
                elif choice == "smlstraight":
                    if 1 and 2 and 3 and 4 in dice:
                        check = True
                    if 2 and 3 and 4 and 5 in dice:
                        check = True
                    if 3 and 4 and 5 and 6 in dice:
                        check = True
                    if check == True:
                        score[9] = 30
                        print("You have claimed your small straight and gained 30 points.")
                        options[9] = ""
                        i = 1
                elif choice == "lrgstraight":
                    if dice == [1,2,3,4,5] or dice == [2,3,4,5,6]:
                        score[10] = 40
                        print("You have claimed your large straight and gained 40 points.")
                        options[10] = ""
                        i = 1
                elif choice == "yahtzee":
                    if [i for i in dice if dice.count(i) == 5]:
                        score[11] = 50
                        print("Congrats! You just got 50 points.")
                        options[11] = ""
                        i = 1
                elif choice == "chance":
                    score[12] = sum(dice)
                    print("You have claimed your chance with a score of: " + str(score[12]))
                    options[12] = ""
                    i = 1
                elif choice == "yahtzeebonus":
                    if options[11] == "yahtzee":
                        print("You need to claim your yahtzee first.")
                    else:
                        if [i for i in dice if dice.count(i) == 5]:
                            score[13] = 100
                            options[13] = ""
                            print("Congrats! You just got 100 points.")
                            i = 1
                elif choice == "h":
                    print("\nHere are your options:")
                    staticoptions = ["ones", "twos", "threes", "fours", "fives", "sixes", "tofakind", "fofakind",
                        "fullhouse", "smlstraight", "lrgstraight", "yahtzee", "chance", "yahtzeebonus", "scratch"]
                    propnames = ["Count of #1 dice", "Count of #2 dice", "Count of #3 dice", "Count of #4 dice",
                                 "Count of #5 dice", "Count of #6 dice", "Three of a kind", "Four of a kind",
                                 "Full house", "Small straight", "Large straight", "Yahtzee", "Chance",
                                 "Yahtzee bonus", "Select a row to scratch"]
                    for x in range(0,15):
                        print('{0:12} = {1}'.format(staticoptions[x], propnames[x]))
                    print("")
                if i != 1 and choice != 'h':
                    print("You entered a valid option, but your dice numbers were not valid.")
            elif choice == "yahtzeebonus":
                if score[13] > 1:
                    score[13] += 100
                    print("Your yahtzee bonus score in now " + str(score[13]))
                    i = 1
                else:
                    print("You have already scratched your yahtzee bonus.")
            elif choice == "scratch":
                check = False
                while check == False:
                    remove = input("Please enter the name of the option you would like to scratch or enter cancel to claim a different option: ")
                    if remove == "cancel":
                        break
                    elif remove == "yahtzee" and "yahtzeebonus" in options:
                        print("You need to remove yahtzeebonus before you can remove this.")
                    else:
                        if remove in options:
                            location = options.index(remove)
                            options[location] = ""
                            score[location] = 0
                            check = True
                            i = 1
                            print("You have scratched your " + remove + " row and have received 0 points for it.")
                        else:
                            print("That is not a scratchable choice please try again.")
            else:
                print("That is not a current option.")