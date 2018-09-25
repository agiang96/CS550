'''
Created on Feb 8, 2018
file: explored.py 
@author: mroch
'''

class Explored(object):
    "Maintain an explored set.  Assumes that states are hashable"

    def __init__(self):
        "__init__() - Create an empty explored set"
        
        # uses python's dictionary to create dictionary
        self.statedict = dict()
        
    def exists(self, state):
        """exists(state) - Has this state already been explored?
        Returns True or False, state must be hashable
        """
        #initially assume state has not been explored 
        exist = False        
        # create a hash for current state
        statehash = hash(state) 
        
        try:
            #creates a list using hash as index
            copydict = self.statedict
            hashlist = copydict[statehash]
            #search list
            for states in hashlist:
                if state == states: #if state exists in dictionary
                    exist = True
                    break
        except KeyError:
            exist = False
        return exist      
    
    def add(self, state):
        """add(state) - add given state to the explored set.  
        state must be hashable and we asssume that it is not already in set
        """
        
        # The hash function is a Python builtin that generates
        # a hash value from its argument.  Use this to create
        # a dictionary key.  Handle collisions by storing 
        # states that hash to the same key in a bucket list.
        # Note that when you access a Python dictionary by a
        # non existant key, it throws a KeyError
        
        statehash = hash(state)
        try:
            #creates a list using hash as indexes
            copydict = self.statedict
            hashlist = copydict[statehash]
            hashlist.append(state)
        #if unable to add to list, add the state to dictionary
        except KeyError:
            copydict = self.statedict
            copydict[statehash] = [state]
            self.statedict = copydict
            
            
