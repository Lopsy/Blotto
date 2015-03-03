__author__ = "Linus"

from random import randint

# This is a simpler way to code strategies, for people like me who are
# intimidated by code like super(RandomStrategy, self).initialise(fields,runs).

# This file contains a strategy which copies a randomly chosen move the
# opponent has made in the past.



def Copier(castles, soldiers):
    # This is the main program. It takes two inputs: "castles" (the number of
    # castles) and "soldiers" (the number of soldiers).

    # Here, put the calculations you want to do before the game begins.

    opponentsMoves = []
    # We can't copy the opponent on the first move, so make our own strat.
    firstMove = [0]*castles # The list [0, 0, ..., 0]
    for i in xrange(soldiers):
        # add a soldier to a random castle
        randomCastle = randint(0, castles-1)
        firstMove[randomCastle] += 1

    # Now, let the game begin.
    while True:

        # Here, calculate your fiendishly clever next move.
        if opponentsMoves == []:
            myMove = firstMove
        else:
            randomIndex = randint(0, len(opponentsMoves)-1)
            myMove = opponentsMoves[randomIndex]


        # Magic line of code, do not change ever:
        opponentsLastMove = yield myMove
        # This plays your move,
        # and stores the opponent's reply in opponentsLastMove.
        
        # Of course, we want to remember it:
        opponentsMoves.append(opponentsLastMove)

        # That's it! This code will loop forever,
        # or until the game ends, whichever comes first.
