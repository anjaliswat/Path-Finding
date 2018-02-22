#!/usr/bin/python

#import state
import sys

class Environment:
    'Map-based environment'

    # Member data
    # elevations: raw data for each position, stored in a list of lists
    #             (each outer list represents a single row)
    # height: number of rows
    # width: number of elements in each row
    # end_x, end_y: location of goal

    def __init__(self, mapfile, energy_budget, end_coords):
        self.elevations = []
        self.height = 0
        self.width = -1
        self.end_x, self.end_y = end_coords
        self.energy_budget = energy_budget
        # Read in the data
        for line in mapfile:
            nextline = [ int(x) for x in line.split() ]
            if self.width == -1:
                self.width = len(nextline)
            elif len(nextline) == 0:
                sys.stderr.write("No data (or parse error) on line %d\n"
                                 % (len(self.elevations) + 1))
                sys.exit(1)
            elif self.width != len(nextline):
                sys.stderr.write("Inconsistent map width in row %d\n"
                                 % (len(self.elevations) + 1))
                sys.stderr.write("Expected %d elements, saw %d\n"
                                 % (self.width, len(nextline)))
                sys.exit(1)
            self.elevations.insert(0, nextline)
        self.height = len(self.elevations)
        if self.end_x == -1:
            self.end_x = self.width - 1
        if self.end_y == -1:
            self.end_y = self.height - 1

        print "height, width:", self.height, self.width
#        print self.height
#        print "width:"
#        print self.width
        print "Destination ", self.end_x, self.end_y
        
        for index, row in enumerate(self.elevations):
            print "Row ", index, str(row)

    def inRange(self, x, y):
        if (x >= 0) and (x <= self.width - 1) and \
            (y >= 0) and (y <= self.height - 1):
                return (True)
        else:
            return (False)
            
    def getCost(self, cnode, nborx, nbory):
        elevNbor = self.elevations[nbory][nborx]
        elevCnode = self.elevations[cnode.y][cnode.x]
        elevDiff = abs(elevCnode - elevNbor)
        #is the move level?
        if (elevNbor == elevCnode):
            cost = 1;
        elif (elevNbor < elevCnode):
            cost = 1 + elevDiff;
        else:
            cost = 1 + pow(elevDiff, 2)

        return (cost)
            
    def getHeuristic(self, x, y):
        heuristic = (abs(self.end_x - x) + abs(self.end_y - y)) + \
            abs(self.elevations[self.end_y][self.end_x] - self.elevations[y][x])
        return (heuristic)
        
    def isDestNode(self, node):
        if node.x == self.end_x and node.y == self.end_y:
            return (True)
        else:
            return(False)
