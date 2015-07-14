#!/usr/bin/env python

from tree import list_to_tree, tree_to_list

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        if not root:
            return
        if root.right:
            self.flatten(root.right)
        if root.left:
            self.flatten(root.left)
        if root.left:
            most_right = root.left
            while most_right.right:
                most_right = most_right.right
            most_right.right = root.right
            root.right = root.left
            root.left = None


def test():
    s = Solution()
    node = list_to_tree([1, 2, None, 3])
    s.flatten(node)
    print(tree_to_list(node))
    node = list_to_tree([1, 2, 3, 4, 5, 6, 7, 8, None, None, 9])
    s.flatten(node)
    print(tree_to_list(node))

if __name__ == '__main__':
    test()
