'''
 Constraint propagation
 file: constraint_prop.py
 Shawn Chua and Alexander Giang
'''
#pseudocode: slides 29 and 30 
def AC3(csp, queue=None, removals=None):
    """AC3 constraint propagation
    """
    # Hints:
    # Remember that:
    #    csp.variables is a list of variables
    #    cps.neighbors[x] is the neighbors of variable x
    if queue != None: #if queue isn't empty, use the queue
            q = queue
    else: #queue is empty 
        q = [] #initialize an empty queue
    
    csp.support_pruning() # MUST BE CALLED before starting to prune
    #fill in queue with binary arcs in CSP
    for x in csp.variables:
        for y in csp.neighbors[x]:
            q.append((x,y))
    # while queue isn't empty 
    while q.__len__() != 0:
        (xi,xj) = q.pop() #get binary constraint (dequeue)
        if revise(csp,xi,xj,removals):
            #if di = Nothing, return false 
            if csp.curr_domains[xi] is None: 
                return False
            else:
                #for each xk in neighbors(xi) - xj
                for xk in (csp.neighbors[xi] - {xj}):
                    q.append((xk,xi)) #enqueue
    return True

def revise(csp,xi,xj,removals):
    pruned = False # initially assume there's no revision
    #for each x in di
    for x in csp.curr_domains[xi]:
        #if y doesn't exist in dj such that constraint holds between x & y
        if all(not csp.constraints(xi, x, xj, y) for y in csp.curr_domains[xj]):
            csp.prune(xi,x,removals) #delete x from di
            pruned = True 
    return pruned
