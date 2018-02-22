class State:
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.cost = 0
        self.heuristic = 0
        self.priority = 0
        self.path = ""
        self.Avalue = 0


    def __repr__(self):
        return (str(self))

    def __str__(self):
        return("["+str(self.x)+","+str(self.y)+","+str(self.cost)+","+str(self.Avalue)+"]")

    def nodeInList(self, lst):
        for index, node in enumerate(lst):
            if self.x==node.x and self.y==node.y:
                return(node, index)

        return (None, None)

