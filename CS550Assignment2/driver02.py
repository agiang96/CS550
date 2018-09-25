'''
driver for graph search problem
Created on Feb 10, 2018
file: driver02.py
@author: mroch
'''

from npuzzle import NPuzzle
from basicsearch_lib02.tileboard import TileBoard
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
from problemsearch import graph_search
import collections
import time
import searchstrategies
from statistics import (mean, stdev)

def tic():
    "Return current time representation"
    return time.time()

def tock(t):
    "Return time elapsed in sec since t where t is the output of tic()"
    return time.time() - t
    
def driver():
    mannytime = [] 
    mannysteps = []
    mannynodesexp = []
    breadytime = []
    breadysteps = []
    breadynodesexp = [] 
    deppytime = []
    deppysteps = []
    deppynodesexp = [] 

    for test in range(2):
        print("Running Test ", test + 1)       
        #Manhattan
        print("solving Manhattan")
        mannyLoopTime = 2
        while(mannyLoopTime > 1):   #for the sake of shorter test times     
            tb = TileBoard(8)
            mannypuzzle = NPuzzle(8, tb.state_tuple(), g=Manhattan.g, h=Manhattan.h)
            currenttime = tic() 
            mannygraph = graph_search(mannypuzzle, verbose=True) # @@@@@TEST OTHER PARAMETERS@@@@@
            mannyLoopTime = tock(currenttime)
        mannytime.append(tock(mannyLoopTime))
        #print(mannygraph) #to compare number of nodes expanded and solution moves
        mannysteps.append(len(mannygraph[1]))
        mannynodesexp.append(mannygraph[0])
        #BreadthFirst
        print("solving BreadthFirst")
        breadypuzzle = NPuzzle(8, tb.state_tuple(), g=BreadthFirst.g, h=BreadthFirst.h)
        currenttime = tic() 
        breadygraph = graph_search(breadypuzzle) # @@@@@TEST OTHER PARAMETERS@@@@@
        breadytime.append(tock(currenttime))
        #print(breadygraph) #to compare number of nodes expanded and solution moves
        breadysteps.append(len(breadygraph[1]))
        breadynodesexp.append(breadygraph[0])      
        #DepthFirst       
        print("solving DepthFirst")
        deppypuzzle = NPuzzle(8, tb.state_tuple(), g=DepthFirst.g, h=DepthFirst.h)
        currenttime = tic()
        deppygraph = graph_search(deppypuzzle) # @@@@@TEST OTHER PARAMETERS@@@@@
        deppytime.append(tock(currenttime))
        #print(deppygraph) #to compare number of nodes expanded and solution moves
        deppysteps.append(len(deppygraph[1]))
        deppynodesexp.append(deppygraph[0])
        #to compare times for each loop
        print("elapsed time: ", tock(currenttime))
    #Mean Values (time, steps, nodes expanded) of each search
    mannytimemean = mean(mannytime)
    mannystepsmean = mean(mannysteps)
    mannynodesmean = mean(mannynodesexp)
    breadytimemean = mean(breadytime)
    breadystepsmean = mean(breadysteps)
    breadynodesmean = mean(breadynodesexp)
    deppytimemean = mean(deppytime)
    deppystepsmean = mean(deppysteps)
    deppynodesmean = mean(deppynodesexp)
    print("Manhattan: ")
    print("Mean Steps: ", mannystepsmean)
    print("Mean Expansion: ", mannynodesmean)
    print("Mean Time: ", mannytimemean)
    print("StDev Steps: ", stdev(mannysteps,mannystepsmean))
    print("StDev Expansion: ", stdev(mannynodesexp,mannynodesmean))
    print("StDev Time: ", stdev(mannynodesexp,mannynodesmean))
    print("BreadthFirst: ")
    print("Mean Steps: ", breadystepsmean)
    print("Mean Expansion: ", breadynodesmean)
    print("Mean Time: ", breadytimemean)
    print("StDev Steps: ", stdev(breadysteps))
    print("StDev Expansion: ", stdev(breadynodesexp))    
    print("StDev Time: ", stdev(breadytime))
    print("DepthFirst: ")
    print("Mean Steps: ", deppystepsmean)
    print("Mean Expansion: ", deppynodesmean)
    print("Mean Time: ", deppytimemean)
    print("StDev Steps: ", stdev(deppysteps))
    print("StDev Expansion: ", stdev(deppynodesexp))
    print("StDev Time: ", stdev(deppytime)) 
    
if __name__ == '__main__':
    driver()
