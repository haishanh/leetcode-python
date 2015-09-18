#!/usr/bin/env python

# TODO

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        def recursive(nums, start, end):
            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            node.left = recursive(nums, start, mid+1)
            node.right = recursive(nums, mid+1, end)
            return node
        return nums and recursive(nums, 0, len(nums)-1)
