# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:12:11 2019

@author: Jerry
"""

from heapq import heappush, heappop

class Hexagon(object):
    g = 0
    h = 0
    def __init__(self, q, r):
        self.q = q
        self.r = r
        
    
class HexGrid(object):
    
    def heuristic(self, start, end):
        return (abs(start.q - end.q) 
                + abs(start.q + start.r - end.q - end.r) 
                + abs(start.r - end.r)) / 2
        
    def explore_neighbours(self, currv):
        # list of neighbours
        n = []
        moves = [(0,-1), (1,-1), (1,0), (0,1), (-1,1), (-1,0)]
        q = currv.q
        r = currv.r
        for dq, dr in moves:
            q2 = q + dq
            r2 = r + dr
            
            # Check that hex is within boundary
            if (q2 >= -3 and q2 <= 3) and (r2 >= -3 and r2 <= 3):
                adj = Hexagon(q2, r2)
                n.append(adj)
        return n
        

def AStarSearch(start, end, grid):
        
    # initialise tree
    start.g = 0
    start.h = grid.heuristic(start, end)
    start.f = start.g + start.h
    
    # Visited, but not expanded nodes
    openv = [] # a min-heap
    # Visited and expanded nodes
    closev = []
    # History of path
    camefrom = []
    
    # Insert start node to openv
    heappush(openv, (start.f, start))
    
    while openv:
        # Pop off node with lowest score
        currv = heappop(openv)[1]
        
        # Find neighbours
        neighbours = grid.explore_neighbours(currv)
        for node in neighbours:
            # If node is the exit square - soln found
            if currv == end:
                return track_path(camefrom, currv)
            
            node.g = currv.g + 1
            node.h = grid.heuristic(currv, end)
            node.f = node.g + node.h
            
            # If neighbour is already in open
            if node in openv:
                # this node already has a lower g, skip it
                index = openv.index(node)
                if openv[index].g <= node.g:
                    continue
                
            elif node in closev:
                index = closev.index(node)
                # Skip if node in closed has lower g
                if closev[index].g <= node.g:
                    continue
                # If a new shorter path has been found, add node back to open
                closev.remove(node)
                openv.append(node)
                
            
            else:
                heappush(openv, (node.f, node))
                # Record parent of neighbour
                camefrom[node] = currv
            
            # Add fully explored node to closed
            closev.append(currv)
    
    return "no solution"

def track_path(camefrom, currv):
    path = []
    # Backtrack path from current hexagon
    while currv in camefrom:
        path.append(currv)
        # Make current hexagon the parent
        currv = camefrom(currv)
    return path


# Testing function
grid = HexGrid()
start = Hexagon(0,0)
end = Hexagon(3,-1)

AStarSearch(start, end, grid)