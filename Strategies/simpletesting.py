__author__ = "Linus"

from simple import Copier

# This is a file to help you test programs written in the simple.py style.
# Instead of penalizing programs which play invalid moves, it crashes.
# Currently uses the "total score" rules, where winning by four is
# twice as good as winning by two.


def quickTest(player1, player2, castles, soldiers, iterations):
    """Call like
    quickTest(Copier, CleverStrat, 10, 100, 9000)"""
    totalscore = 0 # positive for P1 winning, negative for P2 winning

    P1 = player1(castles, soldiers)
    P2 = player2(castles, soldiers)

    move1 = P1.next()
    move2 = P2.next()
    
    for i in xrange(iterations):
        totalscore += score(move1, move2, castles, soldiers)
        move1, move2 = P1.send(move2), P2.send(move1)

    return totalscore
        
def score(move1, move2, castles, soldiers):
    check(move1, castles, soldiers)
    check(move2, castles, soldiers)

    total = 0
    for i in xrange(castles):
        if move1[i] > move2[i]: total += 1
        if move1[i] < move2[i]: total -= 1

    return total


def check(move, castles, soldiers):
    assert(all(a == int(a) for a in move))
    assert(sum(move) == soldiers)
    assert(len(move) == castles)
    move[0]
