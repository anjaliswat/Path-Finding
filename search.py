import environment
import sys
import state
import operator
import solution

class Search:
    def __init__(self, initial_state, env, energy_budget):
        self.initial_state = initial_state
        self.energy_budget = energy_budget
        self.env = env
        self.frontier = [initial_state]
        self.solution = 0
        self.visited = []

    def nodeVisited(self, x, y):
        for node in self.visited:
            if x == node.x and y == node.y:
              return (True)
        return (False)

    def addToFrontier(self, nbor):
        flen = len(self.frontier)
        if (flen == 0):
            print "Append on empty frontier: ", str(nbor)
            self.frontier.append(nbor)
            return

        #check if new nbor allready exists on the frontier list.
        for node in self.frontier:
            if nbor.x == node.x and nbor.y == node.y:
                #remove the existing node on frontier if new node has smaller avalue
                if (nbor.Avalue < node.Avalue):
                    print "Replacing node on frontier: ", str(node)
                    self.frontier.remove(node)
                else:
                    print "Existing node on frontier with lower val: ", str(node)
                    return


        #not on frontier list, so add
        for index, node in enumerate(self.frontier):
            if (node.Avalue > nbor.Avalue):
                print "Insert at index: ", index, str(nbor)
                self.frontier.insert(index, nbor)
                return
            else:
                if (index == flen-1):
                    print "Append at index: ", index, str(nbor)
                    self.frontier.append(nbor)




    def processNeighbor(self, cnode, xn, yn, direction):
        nborx = cnode.x + xn;
        nbory = cnode.y + yn
        print "Processing Nbor:", nborx, nbory

        #check if new nbor is a valid node in env.
        if not self.env.inRange(nborx, nbory):
            print "....out of Range"
            return

        #check if new nbor has allready been visited thru a different path
        if self.nodeVisited(nborx, nbory):
            return

        nbor = state.State(nborx, nbory)
        nbor.cost = cnode.cost + self.env.getCost(cnode, nborx, nbory)
        nbor.heuristic = self.env.getHeuristic(nborx, nbory)
        nbor.Avalue = nbor.cost + nbor.heuristic
        nbor.path = cnode.path + direction

        self.addToFrontier(nbor)

    def search(self):
        self.x = 0
        self.y = 0

        while len(self.frontier) != 0:
            print "frontier:", str(self.frontier)

            current_state = self.frontier[0]
            self.frontier.remove(current_state)

            if self.env.isDestNode(current_state):
                if current_state.cost <= self.energy_budget:
                    self.solution = solution.Solution(current_state.path, current_state.cost)
                    return (self.solution, self.frontier, self.visited)

            #process North, East, South, West in that order
            self.processNeighbor(current_state, 0, 1, "N")
            self.processNeighbor(current_state, 1, 0, "E")
            self.processNeighbor(current_state, 0, -1, "S")
            self.processNeighbor(current_state, -1, 0, "W")

            self.visited.append(current_state)

