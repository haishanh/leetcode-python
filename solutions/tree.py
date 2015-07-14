#!/usr/bin/env python
# my tree module

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def list_to_tree(l):
    '''l is a list reprenting a tree'''
    if not l:
        return None
    # stack to store the node in the bottom of the tree
    stack = []
    root = TreeNode(l[0])
    stack.append(root)
    i = 1
    length = len(l)
    while stack:
        new_stack = []
        for node in stack:
            if i < length and l[i]:
                new = TreeNode(l[i])
                node.left = new
                new_stack.append(new)
            elif i < length:
                node.left = None
            else:
                return root
            i += 1
            if i < length and l[i]:
                new = TreeNode(l[i])
                node.right = new
                new_stack.append(new)
            elif i < length:
                node.right = None
            else:
                return root
            i += 1
        stack = new_stack


def tree_to_list(root):
    '''root is the root of a TreeNode tree'''
    if not root:
        return []
    res = []
    stack = [root]
    while stack:
        new_stack = []
        count = 0
        for node in stack:
            if node:
                new_stack.append(node.left)
                new_stack.append(node.right)
                res.append(node.val)
                count += 1
            else:
                res.append(None)
        if count <= 0:
            while res[-1] == None:
                res.pop()
            return res
        stack = new_stack


def prt_tree(root):
    print(tree_to_list(root))
