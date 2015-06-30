#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head:
            return
        if not head.next:
            return head
        old = None
        node = head
        while node.next:
            the_next = node.next
            node.next = old
            old = node
            node = the_next
        node.next = old # this is important
        return node


def gen_list_node(n):
    l = range(n)
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
    x = gen_list_node(10)
    print(str_list_node(x))
    y = s.reverseList(x)
    print(str_list_node(y))

if __name__ == '__main__':
    test()
