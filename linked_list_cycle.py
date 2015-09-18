#!/usr/bin/env python
from __future__ import print_function


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        d = {}
        node = head
        while node:
            if node in d:
                return True
            d[node] = 1
            node = node.next
        return False

head = ListNode(0)
node1 = ListNode(1)
head.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(3)
node2.next = node3
node4 = ListNode(4)
node3.next = node4
node5 = ListNode(5)
node4.next = node5 # loop
node6 = ListNode(6)
node5.next = node6
node7 = ListNode(7)
node6.next = node7

s = Solution()
x = s.hasCycle(head)
print(x)
