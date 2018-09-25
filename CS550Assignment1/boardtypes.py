'''
file: boardtypes.py
author: Alex Giang
class: CS550 Artificial Intelligence
'''
import math
import random
import copy

from board import Board

class TileBoard(Board):
    def __init__(self, n, force_state=None):
        "TileBoard(n, force_state) Creates an n-puzzle of size n."
        self.boardsize = size = int(math.sqrt(n+1)) 
        
        if isinstance(size, float):
            raise ValueError("Board size must be 1 less than a perfect square, " 
                             + "such as 8, 15, 24, etc")

        # Create the initial state
        tilesList = [x+1 for x in range(n)]
        tilesList.append(None)
        solvable = False
        
        while not solvable:
            random.shuffle(tilesList)            
            # Compute inversion order length defined in A01
            length = 0
            for i in range(len(tilesList)):
                perm = tilesList[i]
                for j in range(i,len(tilesList)):
                    if tilesList[j] != None and perm != None and \
                    tilesList[j] < perm:
                            length += 1
            # Deals with empty tile condition 
            if size % 2 == 0:
                length += math.floor(tilesList.index(None) / size)+1
            solvable = length % 2 == 0
                    
        # initialize the board after shuffle
        super(TileBoard, self).__init__(size, size)
        for row in range(size):
            for col in range(size):
                tile = tilesList[row*size + col]
                if tile:                    
                    self.place(row, col, tile)
                else:
                    self.empty = (row, col)        
    
    def __eq__(self, other):
        "Check if two tile boards are in the same state. "
        pair = ()
        eq = True
        for (this_board, other_board) in pair(self.state_tuple(), 
                                           other.state_tuple()):
            eq = this_board == other_board
            if not eq:
                break
        return eq
    
    def state_tuple(self):
        "Flatten the list of list representation of the board & cast it to a \
        tuple."
        flatList = []
        # Merge the items in each list of lists
        for tupList in self.board:
            for x in tupList:
                flatList.append(x)
        return tuple(flatList)
    
    def get_actions(self):
        "Return list of possible moves in [row_delta,col_delta] format"       
        moves = []
        up = [-1,0]
        down = [1,0]        
        left = [0,-1]
        right = [0,1]
        none = [0,0]
                        
        # find Blank Tile to know the row and column
        for i in range(self.get_rows()):
            for j in range(self.get_cols()):
                if self.get(i,j) == None:
                    row = i
                    col = j
                    self.blank = (i,j)
                    
        # Knowing row and column make it easy to check for available actions
        if row-1 >= 0:
            moves.append(up)
        if row+1 <= self.get_rows()-1:
            moves.append(down)
        if col-1 >= 0:
            moves.append(left)
        if col+1 <= self.get_cols()-1:
            moves.append(right)
        else:
            moves.append(none)             
        return moves
            
    def move(self, offset):
        "move - Move the empty space by [delta_row, col_delta] and return new \
        board"
                                                                                
        # Current row and column of empty space "blank"
        (row, col) = self.blank        
        [delta_row, col_delta] = offset
        # calculate move if possible
        row_move = row + delta_row
        col_move = col + col_delta
        if offset not in self.get_actions():
            raise ValueError("Can't do this move")
            input()

        # Copy board with desired move
        newboard = copy.deepcopy(self)
        newboard.place(row, col, self.get(row_move, col_move))
        newboard.place(row_move, col_move, None)
        newboard.blank = (row_move, col_move)        
        return newboard
    
    def solved(self):
        "solved - Is the puzzle solved?"
        temp = 0
        # 1st condition: empty space must be in center
        center = (self.boardsize-1) / 2
        solved = self.blank == (center, center)
        
        # 2nd condition: check if tiles are in order     
        if solved:
            for tiles in self.state_tuple():
                if tiles:
                    solved = tiles == temp + 1
                    if not solved:
                        break
                    temp = tiles
                    
        return solved
    