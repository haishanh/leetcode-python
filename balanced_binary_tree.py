#!/usr/bin/env python

# TODO balanced binary tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        stack = []
        left_depth = 0
        right_depth = 0
        tmp = root
        def get_depth(node):
            stack = []
            tmp = node
            depth = 0
            if tmp.left:
                stack.push((1, tmp.left))
                depth += 1
            if tmp.right:
                stack.push(tmp.right)
                depth += 1
            if not tmp.left and not tmp.right:
                tmp = stack.pop()


        if tmp.left:
            stack.push(tmp.left)
            left_depth += 1
        elif tmp.right:
            stack.push(tmp.right)

        pass
