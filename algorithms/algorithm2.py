# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 19:23:51 2020

@author: admin
"""

## reduce problems to the set of 
## greedy algorithms get a good enough solution 
##knapsack problem 0-1 problem and continous problem 
## part of optimisatio problems finding the mostest, leastest

## brute force generate all possible combinations  exponential in nature 

class Food(object):
    def __init__(self, n, v, w):
        self.name = n 
        self.value = v
        self.calories = w
        
    def getValue(self):
        return self.value 
    
    def getCost(self):
        return self.calories
    
    def getDensity(self):
        return self.getValue()/self.getCost()
    
    def __str__(self):
        return str(self.name) + ': <' + str(self.value)\
             + ',' + str(self.calories) + '>'
    
    
def buildMenu(names, values, calories):
    menu = []    
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
            
    return menu
    
def greedy(items, maxCost, keyFunction):
    
    itemsCopy = sorted( items, key = keyFunction, reverse = True)
        
    result = []
    totalValue, totalCost = 0.0 , 0.0
        
    for i in range(len(itemsCopy)):
        if totalCost + itemsCopy[i].getCost() <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
                
    return (result , totalValue)
    
    
def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken =', val)
        
    for item in taken:
        print('  ', item)
            
            
            
def testGreedys(food, maxUnits):
        
    print('use greedy by value')
        
    testGreedy(foods, maxUnits, Food.getValue)    
    print('use greedy by cost')
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
        
    print('use greedy by density')
    testGreedy(foods, maxUnits, Food.getDensity)
        
        
        
names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola' , 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 750)

## implementing a decision tree 

def maxVal(toConsider, avail):
    """ Assumes toConsider a list of items, avail is the weight available
    Returns a tuple of the total value of a solution to the knapsack problem
    and the items of the solution
    
    toConsider. those items that the nodes higher up have not yet considered
    avail - the amount of space still available
    
    so at every node we take or not take the item in the result and 
    get it out of the consdieration
    """
    
    if toConsider == [] or  avail == 0:
        result = (0, ())
        
    elif int(toConsider[0].getCost()) > avail:
        result = maxVal(toConsider[1:], avail)
        
    else:
        nextItem = toConsider[0]
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getCost())
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        
        else:
            result = (withoutVal, withoutToTake)
        
    return result

 
#val , list12  = (maxVal(foods, 750)  )  
#print(val)
#for item in list12:
 #   print(item)
    
 
 
class Node(object):
     def __init__(self, name):
         self.name = name 
         
     def getName(self):
         return self.name 
     
     def __str__(self):
            return self.name
        
        
class Edge(object):
    def __init__(self, src, dest):
        """ assume src and obj are nodes"""
        self.src = src
        self.dest = dest
        
        
    def getSource(self):
        return self.src
    
    def getDestination(self):
        return self.dest
    
    def __str__(self):
        return self.src.getName() + '->'\
        + self.dest.getName()
        
        
        
class Digraph(object):
    
    """ edges is a dictionary mapping each node to a list
    of its children in an adjacency list implementatio of digraphs
    each node is mapped to a list of its children nodes"""
    
    def __init__(self):
        self.edges =  {}
        
        
        
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
    
        else:
            self.edges[node] = []
            
    def addEdge(self, edge):
        
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
        
    
    def childrenOf(self, node):
        return self.edges[node]
    
    def hasNode(self, node):
        return node in self.edges
    
    
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
        
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                + dest.getName() + '\n'
        return result[:-1] # omit final new line 
        
    
class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)
        
        
        
def DFS(graph, start, end, path, shortest, toPrint):
    path = path + [start]
    if start == end:
        return path 
    
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                
                if newPath != None:
                    shortest = newPath
    return shortest


def shortestPath(graph, start, end):
    return DFS(graph, start, end, [], None)
        
        
        
        
        
    
    
    
    
    
            
        
        
        
    
    
    
        