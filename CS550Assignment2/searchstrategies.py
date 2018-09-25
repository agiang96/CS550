"""
file: searchstrategies.py

Module to provide implementations of g and h for various search strategies.
In each case, the functions are class methods as we don't need an instance
of the class.  

If you are unfamiliar with Python class methods, Python uses a function
decorator (indicated by an @ to indicate that the next method is a class
method).  Example:

class SomeClass:
    @classmethod
    def foobar(cls, arg1, arg2):
        "foobar(arg1, arg2) - does ..."
        
        code... class variables are accessed as cls.var (if needed)
        return computed value

A caller would import SomeClass and then call, e.g. :  
    SomeClass.foobar("hola","amigos")

Contains g and h functions for:
BreadFirst - breadth first search
DepthFirst - depth first search
Manhattan - city block heuristic search.  To restrict the complexity of
    this, you only need handle heuristics for puzzles of an odd length
    with solutions that contain the blank in the middle and numbers going
    from left to right in each row, e.g.:
        123
        4 5
        678
    When mulitple solutions are allowed, the heuristic becomes a little more
    complex as the city block distance must be estimated to each possible solution
    state. 
"""

import math
from basicsearch_lib02.board import *
from basicsearch_lib02.queues import *
from basicsearch_lib02.searchrep import *
from basicsearch_lib02.tileboard import *

# For each of the following classes, create classmethods g and h
# with the following signatures
#       @classmethod
#       def g(cls, parentnode, action, childnode):
#               return appropritate g value
#       @classmethod
#        def h(cls, state):
#               return appropriate h value
 

class BreadthFirst(object):
    "BredthFirst - breadthfirst search"
    @classmethod
    def g(cls, parentnode, action, childnode):
        return parentnode.depth + 1
    @classmethod
    def h(cls, state):
        return 0

class DepthFirst(object):
    "DepthFirst - depth first search"
    @classmethod
    def g(cls, parentnode, action, childnode):
        return (parentnode.depth + 1) * -1
    @classmethod
    def h(cls, state):
        return 0
        
class Manhattan(object):
    "Manhattan Block Distance heuristic"
    @classmethod
    def g(cls, parentnode, action, childnode):
        return parentnode.depth + 1

    @classmethod
    def h(cls, state):
        goalstate = []
        cost=0
        #generically creates the goal state for N-puzzle
        #ex: goalstate[1,2,3,4,None,5,6,7,8] for an 8-puzzle
        for i in range(state.boardsize**2):
            goalstate.append(i + 1)
        goalstate[(int)(state.boardsize**2 / 2)] = None #add blank node
        #shift the nodes after the None
        for j in range((int)(state.boardsize**2 / 2), (int)(state.boardsize**2 - 1)):                                                   
            goalstate[j + 1] = j + 1
                
        goaltuple = tuple(goalstate) #force_state only takes tuples
        tempboard = TileBoard((int)(state.boardsize**2 - 1), force_state=goaltuple)
        for row in range(state.boardsize):
            for col in range(state.boardsize):
                for row2 in range(state.boardsize):
                    for col2 in range(state.boardsize):
                        if(tempboard.board[row][col] == state.board[row2][col2]):
                            cost += abs(row-row2) + abs(col-col2)
        return cost       
                
                