'''
 file: backtrack.py
 Shawn Chua and Alexander Giang
'''
from csp_lib.backtrack_util import (first_unassigned_variable, 
                                    unordered_domain_values,
                                    no_inference)
# pseudocode: slide 44

def backtracking_search(csp,
                        select_unassigned_variable=first_unassigned_variable,
                        order_domain_values=unordered_domain_values,
                        inference=no_inference):
    """backtracking_search
    Given a constraint satisfaction problem (CSP),
    a function handle for selecting variables, 
    a function handle for selecting elements of a domain,
    and a set of inferences, solve the CSP using backtrack search
    """
    # See Figure 6.5] of your book for details

    def backtrack(assignment):
        """Attempt to backtrack search with current assignment
        Returns None if there is no solution.  Otherwise, the
        csp should be in a goal state.
        """
        # if all variables assigned, return assignment
        if assignment.__len__() == csp.variables.__len__():
            return assignment 
        var = select_unassigned_variable(assignment,csp)
        #for each value in order domain
        for value in order_domain_values(var, assignment, csp):
            #if value is consistent with assignment (no conflicts)
            if csp.nconflicts(var,value,assignment) == 0:
                csp.assign(var,value,assignment) #assign value
                #suppose() value for interference() & restore()
                removals = csp.suppose(var,value)
                #check if there's inference
                if inference(csp, var, value, assignment, removals):
                    result = backtrack(assignment)
                    #if backtrack did not fail, return result
                    if result is not None: 
                        return result
                # either value inconsistent or further exploration failed
                csp.restore(removals) #undo suppose
        # restore assignment to its state at top of loop and try next value
        csp.unassign(var,assignment) 
        return None #failure
        

    # Call with empty assignments, variables accessed
    # through dynamic scoping (variables in outer
    # scope can be accessed in Python)
    result = backtrack({})
    assert result is None or csp.goal_test(result)
    return result
