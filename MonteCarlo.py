class Node(object):
    """Node in MC tree representing the board state.
    Records its Q and P."""
    
    def __init__(self, parent, prior):
        self.parent = parent
        self.children = {}
        
        self.N = 0 # number of times a was taken from s
        self.W = 0 # total value of next state
        self.Q = 0 # mean action value
        self.P = prior # Prior probabilities from NN
        self.U = 0
    
    def calcU(self):
        """Calculate and set upper confidence bound."""
        c_puct = 1 # exploitation vs exploration hyperparam
        u = (c_puct * self.P * np.sqrt(self.parent.N) / (1 + self.N))
        
        self.U = self.Q + u
        return
    
    def select(self):
        """Choose best move based on U values."""
        maxU = 0
        node = None
        # chooose the best action by maximising U
        for child in self.children:
            if calcU > maxU:
                maxU = calcU
                node = child
        
        return child
    
    def expand(self, actions):
        """Expand one more node.
        Takes in: list of (moves, probability of move) from NN"""
        for move, prob in action:
            # Create new children if new state has not been explored
            if move not in self.children:
                self.children[move] = Node(self, prob)

    def update():
        """Back propagate values from leaf back up the tree."""
        self.N += 1
        self.W += v
        self.Q = W/N