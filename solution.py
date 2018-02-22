class Solution:
    def __init__(self, moves_so_far,cost_so_far):
        self.moves_so_far = moves_so_far
        self.cost_so_far = cost_so_far

    def __repr__(self):
        return (str(self))
    
    def __str__(self):
        return ("[Cost: " + str(self.cost_so_far) + " " + self.moves_so_far +"]")