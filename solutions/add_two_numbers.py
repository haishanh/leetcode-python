#!/usr/bin/env python
from __future__ import print_function


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_rem(n):
    return n % 10, n // 10


def gen_list_node(n):
    rem, result = get_rem(n)
    tmp_node = ListNode(rem)
    head = tmp_node
    while result:
        rem, result = get_rem(result)
        new_node = ListNode(rem)
        # print(new_node.val)
        tmp_node.next = new_node
        tmp_node = new_node
    return head


def resolve_list_node(node):
    fac = 1
    result = 0
    while node:
        result += node.val * fac
        fac *= 10
        node = node.next
    return result


def str_node(node):
    s = ''
    while node:
        if node.next:
            s += "%d -> " % (node.val)
        else:
            s += "%d" % (node.val)
        node = node.next
    return s


class Solution:
    def addTwoNumbers(self, l1, l2):
        pass


def test(n1, n2):
    node1 = gen_list_node(n1)
    print('l1 node is: %s' % str_node(node1))
    node2 = gen_list_node(n2)
    print('l2 node is: %s' % str_node(node2))
    result_node = gen_list_node(resolve_list_node(node1) +
                                resolve_list_node(node2))
    print('RESULT node is: %s\n' % str_node(result_node))
    return resolve_list_node(result_node)


def run():
    assert test(342, 465) == 342 + 465
    assert test(1234, 11) == 1234 + 11
    assert test(5, 5) == 5 + 5

if __name__ == '__main__':
    run()
