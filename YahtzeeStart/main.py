# making changes to comment


from time import sleep
import time
import os
import random

from constants import *
import scoring
from scorecard import *
from playing import *


# TODO: write main AFTER you have written and tested each function
def main():
    """
    create a list of lists for the scorecard
    set userTurn to false
    call resetScorecard

    while there are still empty items in either scorecard
        swap players
        call updateScorecard
        call displayScorecard
        if it's the user's turn
            print a message and pause briefly
            call userPlay
        else
            print a message and pause breifly
            call computerPlay
        end if
     end while
     call updateScorecard
     call displayScorecard
     determine who won and display a message

    """

    # this list of list consists of two elements
    # sets indexes to None
    # first part consists of user scorecard, second part computer scorecard
    theScorecard = [[None] * (constants.TOTAL + 1), [None] * (constants.TOTAL + 1)]
    userTurn = False
    # calls resetScorecard
    resetScorecard(theScorecard)

    while theScorecard[USER].count(-1) > 0 and theScorecard[COMPUTER].count(-1) > 0:
        # set userTurn to opposite to swap
        userTurn = not userTurn
        updateScorecard(theScorecard)
        displayScorecards(theScorecard)
        if userTurn:
            print("It's your turn.")
            sleep(1)
            # call userPlay
            userPlay(theScorecard[USER])
        else:
            print("Computers turn.")
            sleep(1)
            computerPlay(theScorecard[COMPUTER])
    updateScorecard(theScorecard)
    displayScorecards(theScorecard)
    if theScorecard[USER][TOTAL] > theScorecard[COMPUTER][TOTAL]:
        print("You won!")
    else:
        print("The computer won!")


# this block is the same all of the time
# when the name of the file is main, call main
if __name__ == '__main__':
    main()
