#!/usr/bin/env python

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        '''recursion way'''
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# Since it's not easy to represent a binary tree in a arry
#.hence this test is ugly hardcoded
def gen_binary_tree():
    left = TreeNode(1)
    right = TreeNode(3)
    m_left = TreeNode(2)
    m_left.left = left
    m_left.right = right
    left = TreeNode(6)
    right =TreeNode(9)
    m_right = TreeNode(7)
    m_right.left = left
    m_right.right = right
    root = TreeNode(4)
    root.left = m_left
    root.right = m_right
    return root

def prt_tree(tree):
    print(tree.val)
    print(tree.left.val, tree.right.val)
    print(tree.left.left.val, tree.left.right.val, tree.right.left.val, tree.right.right.val)

def test():
    root = gen_binary_tree()
    prt_tree(root)
    s = Solution()
    prt_tree(s.invertTree(root))

if __name__ == '__main__':
    test()
