"""
    This module contains all of the functions related to working with the scorecard
"""

from constants import *
from scoring import *
from playing import clear


# TODO: write resetScorecard and updateScorecard
def resetScorecard(scorecard):
    """ takes the 2-d list that represents the scorecard as it's parameter and
    sets each of the individual values for the user and the computer to the constant empty.
    The subtotal, bonus and total should be set to 0.
    It does not return a value but the scorecard is altered by the function
    """
    # index starts at YAHTZEE
    for i in range(YAHTZEE + 1):
        scorecard[USER][i] = EMPTY
        scorecard[COMPUTER][i] = EMPTY

    for i in range(SUBTOTAL, TOTAL + 1):
        scorecard[USER][i] = 0
        scorecard[COMPUTER][i] = 0


def updateScorecard(scorecard):
    """ takes the 2-d list that represents the scorecard as it's parameter and
    calculates the subtotal, bonus and total for both the user and the computer.
    It does not return a value but the scorecard is altered by the function
    """
    # for subtotal
    if scorecard[USER] and scorecard[COMPUTER] != EMPTY:
        scorecard[USER][SUBTOTAL] = 0
        scorecard[COMPUTER][SUBTOTAL] = 0
        for i in range(ONES, SIXES + 1):
            if scorecard[USER][i] != EMPTY:
                scorecard[USER][SUBTOTAL] += scorecard[USER][i]
            if scorecard[COMPUTER][i] != EMPTY:
                scorecard[COMPUTER][SUBTOTAL] += scorecard[COMPUTER][i]

    # for bonus
    if scorecard[USER][SUBTOTAL] > int(63):
        scorecard[USER][BONUS] = int(35)
    if scorecard[COMPUTER][SUBTOTAL] > int(63):
        scorecard[COMPUTER][BONUS] = int(35)

    # for total score
    if scorecard[USER] and scorecard[COMPUTER] != EMPTY:
        scorecard[USER][TOTAL] = 0
        scorecard[COMPUTER][TOTAL] = 0
        for i in range(THREE_OF_A_KIND, BONUS + 1):
            if scorecard[USER][i] != EMPTY:
                scorecard[USER][TOTAL] += scorecard[USER][i]
            if scorecard[COMPUTER][i] != EMPTY:
                scorecard[COMPUTER][TOTAL] += scorecard[COMPUTER][i]









def formatCell(value):
    return "" if value < 0 else str(value)


def displayScorecards(scorecard):
    labels = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes",
              "3 of a Kind", "4 of a Kind", "Full House", "Small Straight", "Large Straight",
              "Chance", "Yahtzee", "Sub Total", "Bonus", "Total Score"]
    lineFormat = "| {3:2s} {0:<15s}|{1:>8s}|{2:>8s}|"
    border = '-' * 39
    uScorecard = scorecard[constants.USER]
    cScorecard = scorecard[constants.COMPUTER]

    #clear()
    print(border)
    print(lineFormat.format("", "  You   ", "Computer", ""))
    print(border)

    for i in range(constants.ONES, constants.SIXES + 1):
        print(lineFormat.format(labels[i], formatCell(uScorecard[i]), formatCell(cScorecard[i]), str(i)))

    print(border)
    print(lineFormat.format(labels[constants.SUBTOTAL], formatCell(uScorecard[constants.SUBTOTAL]), formatCell(cScorecard[constants.SUBTOTAL]), ""))
    print(border)
    print(lineFormat.format(labels[constants.BONUS], formatCell(uScorecard[constants.BONUS]), formatCell(cScorecard[constants.BONUS]), ""))
    print(border)

    for i in range(constants.THREE_OF_A_KIND, constants.YAHTZEE + 1):
        print(lineFormat.format(labels[i], formatCell(uScorecard[i]), formatCell(cScorecard[i]), str(i)))

    print(border)
    print(lineFormat.format(labels[constants.TOTAL], formatCell(uScorecard[constants.TOTAL]), formatCell(cScorecard[constants.TOTAL]), ""))
    print(border)



