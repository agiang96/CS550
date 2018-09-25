'''
Created on Feb 22, 2015

@author: mroch
'''

import time
import datetime
import ai
import checkerboard
from copy import deepcopy
# tonto - Professor Roch's not too smart strategy
# You are not given source code to this, but compiled .pyc files
# are available for Python 3.5 and 3.6 (fails otherwise).
# This will let you test some of your game logic without having to worry
# about whether or not your AI is working and let you pit your player
# against another computer player.
#
# Decompilation is cheating, don't do it.
#import tonto

# human - human player, prompts for input    
import human
import boardlibrary # might be useful for debuggingimport tonto

#Tonto is another AI that can play against our AI
import imp
import sys
major = sys.version_info[0]
minor = sys.version_info[1]
modpath = "__pycache__/tonto.cpython-{}{}.pyc".format(major, minor)
tonto = imp.load_compiled("tonto", modpath)


def elapsed(earlier, later):
    """elapsed - Convert elapsed time.time objects to duration string
    
    Useful for tracking move and game time.  Example pseudocode:
    
    gamestart = time.time()
    
    while game not over:
        movestart = time.time()
        ...  logic ...
        current = time.time() 
        print("Move time: {} Game time: {}".format(
            elapsed(movestart, current), elapsed(gamestart, current))
    
    
    """
    return time.strftime('%H:%M:%S', time.gmtime(later - earlier))
           

def Game(red=tonto.Strategy, black=ai.Strategy, maxplies=5, init=None, verbose=True, firstmove=0):
    """Game(red, black, maxplies, init, verbose, turn)
    Start a game of checkers
    red,black - Strategy classes (not instances)
    maxplies - # of turns to explore (default 10)
    init - Start with given board (default None uses a brand new game)
    verbose - Show messages (default True)
    firstmove - Player N starts 0 (red) or 1 (black).  Default 0. 
    """
    
    # Don't forget to create instances of your strategy,
    # e.g. black('b', checkerboard.CheckerBoard, maxplies)
    red_dude = red('r', checkerboard.CheckerBoard, maxplies)
    black_dude = black('b', checkerboard.CheckerBoard, maxplies)
    maxturns = 40
    if init is None:
        board = checkerboard.CheckerBoard()
    else: 
        board = init
    while not board.is_terminal()[0] and maxturns > 0:
        board.update_counts()
        if firstmove == 0:
            #red moves first
            [board1, red_action] = red_dude.play(board)    
            print(board1)
            if red_action is None: #Player forfeits
                print("Red forfeited! Black dude won")
                break
            [board2, black_action] = black_dude.play(board1)
            print(board2)
            board = board2
        elif firstmove == 1:
            [board2, black_action] = black_dude.play(board1)
            print(board2)
            #red goes
            [board1, red_action] = red_dude.play(board2)    
            print(board1)
            board = board1
        maxturns -= 1
        if board.is_terminal()[0]:
            #game is over
            print (board.is_terminal()[1],' won!!!!!!')
            break
        if maxturns == 0:
            print('Game Over! Draw! No one won but you all are losers')
            break


if __name__ == "__main__":
    Game()   
                    
            
        

    
    
