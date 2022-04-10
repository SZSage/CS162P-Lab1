"""
    This module contains all of the functions related to playing the game
"""

from os import system, name
from time import sleep
import random

import constants
from validation import getIntInRange
import scoring


# TODO: write userPlay.  I've written the rest for you.
def userPlay(uScorecard):
    """
        create an empty list for the dice you're keeping
        create another empty list for the dice that you're rolling
        set itemIndex to -1
        set rollCount to 0
        while rollCount < 3 and there are less than 5 dice in keeping
            call roll (the number of dice is 5 - the number of dice that you're keeping)
            increment rollCount
            print a message and the dice
            if rollCount < 3
                call getKeeping
            else
                call moveRollToKeep
            end if
            print a message and the dice
        itemIndex = call getScorecardItme
        set the element in the user's scorecard based on the score of the dice in keeping
    """
    keeping = []
    rolling = []
    itemIndex = -1
    rollCount = 0
    while rollCount < 3 and len(keeping) < 5:
        roll(5 - len(keeping), rolling)
        rollCount += 1
        print("You rolled: ")
        displayDice(rolling)
        if rollCount < 3:
            getKeeping(rolling, keeping)
        else:
            moveRollToKeep(rolling, keeping)
        print("Your dices: ")
        displayDice(keeping)
    itemIndex = getScorecardItem(uScorecard)
    uScorecard[itemIndex] = scoring.score(itemIndex, keeping)


def computerPlay(cScorecard):
    keeping = []
    itemIndex = -1
    roll(5, keeping)
    print("The dice the computer rolled: ")
    displayDice(keeping)
    sleep(1)
    itemIndex = getComputerScorecardItem(cScorecard, keeping)
    cScorecard[itemIndex] = scoring.score(itemIndex, keeping)


def roll(numDice, dice):
    dice.clear()
    for i in range(numDice):
        dice.append(random.randint(1, 6))


def moveRollToKeep(rolling, keeping):
    for d in rolling:
        keeping.append(d)
    rolling.clear()


def getComputerScorecardItem(cScorecard, keeping):
    indexOfMax = 0
    max = 0
    for i in range(constants.YAHTZEE + 1):
        if cScorecard[i] == constants.EMPTY:
            score = scoring.score(i, keeping)
            if score >= max:
                max = score
                indexOfMax = i
    return indexOfMax


def getScorecardItem(uScorecard):
    itemIndex = getIntInRange(constants.ONES, constants.YAHTZEE, "What item would you like to score? ")
    while uScorecard[itemIndex] != constants.EMPTY:
        print("Oops!  You've already scored that item. ")
        itemIndex = getIntInRange(constants.ONES, constants.YAHTZEE, "What item would you like to score? ")
    return itemIndex


def getKeeping(rolling, keeping):
    indexes = input("Which dice would you like to keep? ").split()
    for s in indexes:
        if s.isdigit() and int(s) < len(rolling):
            keeping.append(rolling[int(s)])
    rolling.clear()


def displayDice(dice):
    lineFormat = "| {0} |"
    border = "*---*"

    for d in dice:
        print(border, end="")
    print()
    for d in dice:
        print(lineFormat.format(d), end="")
    print()
    for d in dice:
        print(border, end="")
    print()


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')