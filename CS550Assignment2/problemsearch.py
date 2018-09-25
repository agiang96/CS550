'''
Created on Feb 10, 2018
file: problemsearch.py
@author: mroch
'''


from basicsearch_lib02.searchrep import (Node, print_nodes)
from basicsearch_lib02.queues import PriorityQueue 
from explored import Explored
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
import time

        
def graph_search(problem, verbose=False, debug=False):
    """graph_search(problem, verbose, debug) - Given a problem representation
    (instance of basicsearch_lib02.representation.Problem or derived class),
    attempt to solve the problem.
    
    If debug is True, debugging information will be displayed.
    
    if verbose is True, the following information will be displayed:
        
        Number of moves to solution
        List of moves and resulting puzzle states
        Example:
        
            Solution in 25 moves        
            Initial state
                  0        1        2    
            0     4        8        7    
            1     5        .        2    
            2     3        6        1    
            Move 1 -  [0, -1]
                  0        1        2    
            0     4        8        7    
            1     .        5        2    
            2     3        6        1    
            Move 2 -  [1, 0]
                  0        1        2    
            0     4        8        7    
            1     3        5        2    
            2     .        6        1    
            
            ... more moves ...
            
                  0        1        2    
            0     1        3        5    
            1     4        2        .    
            2     6        7        8    
            Move 22 -  [-1, 0]
                  0        1        2    
            0     1        3        .    
            1     4        2        5    
            2     6        7        8    
            Move 23 -  [0, -1]
                  0        1        2    
            0     1        .        3    
            1     4        2        5    
            2     6        7        8    
            Move 24 -  [1, 0]
                  0        1        2    
            0     1        2        3    
            1     4        .        5    
            2     6        7        8    
        
        If no solution were found (not possible with the puzzles we
        are using), we would display:
        
            No solution found
    
    Returns a tuple (path, nodes_explored) where:
    path - list of actions to solve the problem or None if no solution was found
    nodes_explored - Number of nodes explored (dequeued from frontier)
    """
    explored = Explored()
    numnodes = 0 
    finished = False

    #create initial state without parent or actions
    currentnode = Node(problem, problem.initial)
    #DepthFirst doesn't create the correct frontier with the default PriorityQueue()
    if(problem.g == DepthFirst.g and problem.h == DepthFirst.h):
        frontier = PriorityQueue(currentnode.get_f()) 
    else:
        frontier = PriorityQueue()
    frontier.append(currentnode)
    
    while not finished:
        currentnode = frontier.pop()
        if debug:   #will print all the steps of traversing thru search
            print(currentnode.__repr__())
        explored.add(currentnode.state)
        if not currentnode.state.solved():
            for nodes in currentnode.expand(problem):
                numnodes += 1
                if not explored.exists(nodes.state):
                    frontier.append(nodes)
                finished = frontier.__len__() == 0
        else:
            finished = True
            
    if verbose: #will print the solution steps per function description
        if(currentnode.solution() == 0): 
            print("No solution found")
        else:
            print("Solution in ", len(currentnode.solution()), " moves")
            print("Initial State")
            print(problem.initial)
            problemcopy = problem.initial
            for moves in range(len(currentnode.solution())):
                print("Move ", moves + 1, " - ", currentnode.solution()[moves])
                problemcopy = problemcopy.move(currentnode.solution()[moves])
                print(problemcopy.__repr__())
    return (numnodes, currentnode.solution())



