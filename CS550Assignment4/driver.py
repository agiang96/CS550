'''
 file: driver.py
 Shawn Chua and Alexander Giang
'''
from csp_lib.sudoku import (Sudoku, easy1, harder1)
from constraint_prop import AC3
from csp_lib.backtrack_util import mrv
from backtrack import backtracking_search


for puzzle in [easy1]:
    easy  = Sudoku(easy1)  # constructing the easy Sudoku problem
    print("Easy Sudoku Problem:")
    easy.display(easy.infer_assignment())
    
    AC3(easy) #Calling Constraint Propagation to solve
    
    print("\n")
    print("After calling AC3:")
    easy.display(easy.infer_assignment())
    
    if not easy.goal_test(easy.curr_domains):
        print("\n")
        print("Backtracking easy problem...")
        result = backtracking_search(easy,select_unassigned_variable=mrv)
        if result:
            print("After backtracking:")
            easy.display(easy.infer_assignment())

            
for puzzle in [harder1]:
    hard  = Sudoku(puzzle)  # constructing the hard Sudoku problem
    print("\n")
    print("Hard Sudoku Problem:")
    hard.display(hard.infer_assignment())
    
    AC3(hard) #Calling Constraint Propagation to solve
    
    print("\n")
    print("After calling AC3:")
    hard.display(hard.infer_assignment())
    
    if not hard.goal_test(hard.curr_domains):
        print("\n")
        print("Backtracking hard problem...")
        result = backtracking_search(hard,select_unassigned_variable=mrv)
        if result:
            print("After backtracking:")
            hard.display(hard.infer_assignment())
    
    