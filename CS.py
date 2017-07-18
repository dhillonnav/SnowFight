from math import*
from random import *

global pattern1, snowballsEachRound, goHam

nextMove = ""
nm = ""

pattern1 = 0

mySnowballsEachRound = []

goHam = False

#def getRandomMove


def getMove (myScore, mySnowballs, myDucksUsed, myMoveHistory,
             opponentsScore, opponentsSnowballs, opponentsDucksUsed, opponentsMoveHistory):

   
    global pattern1, snowballsEachRound, goHam

    mySnowballsEachRound.append(mySnowBalls)

    if goHam == True:
        if mySnowballs > 0:
            return "THROW"
        else:
            goHam == False

    if nextMove != "":
        nm = nextMove
        nextMove = ""
        return nm

    if len(moveHistory) == 0:
        return "THROW"
    
    if len(moveHistory) == 1:
        if opponentsMoveHistory[-1] == "THROW":
            return "RELOAD"
        elif opponentsMoveHistory[-1] == "RELOAD":
            return choice([60*["RELOAD"],40*["DUCK"]])

    
    if len(myMoveHistory) > 1:
        if opponentsMoveHistory[i - 1] == "THROW" and mySnowBallsEachRound[-1] == 0 and mySnowballsEachRound[-2] != 0:
            pattern1 += 1

    
    if myScore == opponentsScore and myScore == 2:
        if mySnowballs > opponentsDucksUsed:
            if opponentsSnowballs == 0:
                return "THROW"
            elif mySnowballs > ((5 - opponentsDucksUsed) + opponentSnowballs):
                goHam = True
                return "THROW"
                
    elif mySnowballs == opponentSnowballs:
        if mySnowballs == 0:
            return "RELOAD"
        else:
            return "THROW"
    #elif mySnowballs > opponentsSnowballs:
       # if 

        
    elif opponentsSnowballs > mySnowballs:
        if mySnowballs == 0 and myDucksUsed < 5:
            if pattern1 > 0:
                if opponentsSnowballs != 0 and myDucksUsed <= 3:
                    nextMove == choice([50*["RELOAD"],50*["DUCK"]])                       
                return "DUCK"
            else:
                return choice([75*["RELOAD"],25*["DUCK"]])

        #elif mySnowballs > 0 and myDucksUsed < 5:
            
                
            
            
##    elif opponentsScore == 2:
##
##    if 
##
##else:
##    if pattern1 > 0:
##            
##
##    

#if Ducksleft == 0:

def correctMove(myScore, mySnowballs, myDucksUsed, myMoveHistory,
                 opponentsScore, opponentsSnowballs, opponentsDucksUsed, opponentsMoveHistory):
    
    move = getMove(myScore, mySnowballs, myDucksUsed, myMoveHistory,
             opponentsScore, opponentsSnowballs, opponentsDucksUsed, opponentsMoveHistory)

    if (30 - len(myMoveHistory)) <= mySnowballs:
        return "THROW"
    
    elif mySnowballs == 10 and move == "RELOAD":
        return "SHOOT"
    
    elif myDucksUsed == 5 and move == "DUCK":
        if mySnowballs > 0:
            return "SHOOT"
        else:
            return "RELOAD"

    else:
        return move

