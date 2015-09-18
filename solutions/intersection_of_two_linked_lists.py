#!/usr/bin/env python


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# hashset solution, O(n+m) time, O(n) or O(m) space
class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        d = {}
        tmp = headA
        while tmp:
            d[tmp] = 1
            tmp = tmp.next
        tmp = headB
        while tmp:
            if d.get(tmp):
                return tmp
            tmp = tmp.next
        return None


def test():
    pass

if __name__ == '__main__':
    test()
