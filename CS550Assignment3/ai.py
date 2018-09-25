
"""
ai - search & strategy module

implement a concrete Strategy class and AlphaBetaSearch
"""

from copy import deepcopy
import abstractstrategy

class Strategy(abstractstrategy.Strategy):
    def __init__(self, player, game, maxplies):
        self.player = player
        self.game = game
        self.maxplies = maxplies
        super(Strategy,self).__init__(self.player, self.game, self.maxplies)
        self.red = 0 #opponent
        self.black = 1 #AI
        
    def utility(self, board):
        corner = [[0,7], [7,0]]
        edge = [[0,1],[0,3],[0,5],[1,0],[3,0],[5,0],[2,7],[4,7],[6,7],[7,2],[7,4],[7,6]]
        currentboard = deepcopy(board)
        #update pawn and king count
        currentboard.update_counts()
        utility = 0
        #determine utility based on number of pawns and kings
        numpawns = currentboard.get_pawnsN()[self.black] - currentboard.get_pawnsN()[self.red]
        if numpawns >= 0: #black has more
            utility += numpawns*3
        elif numpawns < 0:
            utility += numpawns*3
        numkings = currentboard.get_kingsN()[self.black] - currentboard.get_kingsN()[self.red]
        if numkings >= 0: #black has more
            utility += numkings*5
        else:
            utility += numkings*5
                
        for r in range (8):
            for c in range (8):
                #determine utility based on distance to king
                if self.maxplayer is currentboard.get(r,c):
                    if board.disttoking(self.player,r) == 1:
                        utility += 0.5
                    elif board.disttoking(self.player,r) == 2:
                        utility += 0.25
                elif self.minplayer is currentboard.get(r,c):
                    if board.disttoking(self.minplayer,r) == 1:
                        utility -= 2
                    elif board.disttoking(self.minplayer,r) == 2:
                        utility -= 3.5
                #determine utility based on edges and corners
                #both will have increase utility but edges will have more        
                if self.maxplayer is currentboard.get(r,c):
                    if corner.__contains__([r,c]):
                        utility += 4
                    elif edge.__contains__([r,c]):
                        utility += 4             
        #determine utility based on lost pieces from next action
        #look at if any AI moves results in a capture
        for actions in currentboard.get_actions(self.maxplayer): 
            if len(actions[1]) == 3:#indicates a capture
                cappiece = currentboard.get(actions[1][2][0], actions[1][2][1])
                if currentboard.ispawn(cappiece):
                    utility += 0.5
                elif currentboard.isking(cappiece):
                    utility += 1
            nextboard = currentboard.move(actions)
            #look at board as a result of our moves
            #determine if the opponent can capture a piece
            for opactions in nextboard.get_actions(self.minplayer):
                if len(opactions) >= 3: #indicates multiple capture
                    utility -=200
                if len(opactions[1]) == 3: #capture
                    utility-=20
                    ourpiece = currentboard.get(opactions[1][2][0], opactions[1][2][1])
                    if nextboard.ispawn(ourpiece):
                        utility -= 50
                    elif nextboard.isking(ourpiece):
                        utility -= 100
        return utility
    
    #does all the searching during playtime
    def play(self, board, hints=True):
        board.update_counts()
        if board.is_terminal()[0]:
            return (board,0)
        s = Strategy(self.player,self.game,self.maxplies)
    
        a_b_s = AlphaBetaSearch(s,self.maxplayer,self.minplayer,maxplies=self.maxplies)
        v = a_b_s.alphabeta(board,self.maxplies)
        newboard = board.move(v[1])
        print("utility: ",v[0])
        print("black pawns", board.get_pawnsN()[1])
        return (newboard,v[1])
        
class AlphaBetaSearch:
    def __init__(self, strategy, maxplayer, minplayer, maxplies = 3, verbose = False):
        self.strategy = strategy
        self.maxplayer = maxplayer
        self.minplayer = minplayer
        
    def alphabeta(self, state, maxplies):
        alpha = float('-inf')
        beta = float('inf')
        #finds the best value for AI
        v = self.max_value(state,alpha,beta, maxplies)
        return v #where v is a tuple of(utility, action)

    # finds action with highest utility for AI    
    def max_value(self, state, alpha, beta, plies):
        bestaction = []
        if state.is_terminal()[0] or plies <= 0: #add self.black
            v = self.strategy.utility(state)
        else:
            v = float('-inf')
            #compares opponents' (minplayer) utility
            for action in state.get_actions(self.maxplayer):
                bestaction = action                
                v = max(v, self.min_value(state.move(action), alpha, beta, plies - 1)[0])
                if isinstance(v,int) | isinstance(v,float):
                    if v >= beta:
                        break
                    else:
                        alpha = max(alpha,v)
                else:
                    if v[0] >= beta:
                        break
                    else:
                        alpha = max(alpha, v[0])
        return (v, bestaction)

    #finds action with lowest utility for AI     
    def min_value(self, state, alpha, beta, plies):
        bestaction = []
        if state.is_terminal()[0] or plies <= 0: #add self.black
            v = self.strategy.utility(state)
        else:
            v = float('inf')
            #compares opponents' (minplayer) utility
            for action in state.get_actions(self.minplayer):
                bestaction = action                
                v = min(v, self.max_value(state.move(action), alpha, beta, plies - 1)[0])
                if isinstance(v,int) | isinstance(v,float):
                    if v <= alpha:
                        break
                    else:
                        beta = min(beta,v)
                else:
                    if v[0] <= alpha:
                        break
                    else:
                        beta = min(beta, v[0])
        return (v, bestaction)
