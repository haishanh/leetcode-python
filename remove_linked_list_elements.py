#!/usr/bin/env python
from __future__ import print_function

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        def remove_node(prev, curr):
            prev.next = curr.next
        node = head
        # if match at the head
        while node and node.val == val:
            node = node.next
        new = node
        if not new:
            return new
        while node:
            while node.next and node.next.val == val:
                remove_node(node, node.next)
            node = node.next
        return new

def gen_list_node(n):
    l = range(1,n)
    old = ListNode(l[-1])
    for i in l[-2::-1]:
        new = ListNode(i)
        new.next = old
        old = new
    return old

def str_list_node(node):
    if not node.next:
        return str(node.val)
    else:
        return str(node.val) + ' -> ' + str_list_node(node.next)

def test():
    s = Solution()
    node = gen_list_node(8)
    print('original :', str_list_node(node))
    new = s.removeElements(node, 3)
    print('3 removed:', str_list_node(new))
    new = s.removeElements(node, 0)
    print('0 removed:', str_list_node(new))
    node = gen_list_node(3)
    print('original :', str_list_node(node))
    new = s.removeElements(node, 2)
    print('2 removed:', str_list_node(new))

    # 1 -> 2 -> 2 -> 1
    old =  ListNode(1)
    new = ListNode(2)
    new.next = old
    old = ListNode(2)
    old.next = new
    new = ListNode(1)
    new.next = old
    node = new
    print('original :', str_list_node(node))
    new = s.removeElements(node, 2)
    print('2 removed:', str_list_node(new))



if __name__ == '__main__':
    test()
