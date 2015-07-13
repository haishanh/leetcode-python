#!/usr/bin/env python

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        processed = {}
        def clone(node):
            if node in processed:
                return processed[node]
            else:
                new = UndirectedGraphNode(node.label)
                processed[node] = new
                for neighbor in node.neighbors:
                    new.neighbors.append(clone(neighbor))
                return new
        return node and clone(node)

def test():
    pass

if __name__ == '__main__':
    test()
