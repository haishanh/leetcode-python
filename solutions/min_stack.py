#!/usr/bin/env python

# TODO
#.Time exceeded

#.Also I think testcase on leetcode.com is not cover all the possible scenarios
class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self._s = []
        self._ordered = []


    # @param x, an integer
    # @return nothing
    def push(self, x):
        self._s.append(x)
        # self._ordered.append(x)
        # self._ordered.sort(reverse=True)
        for i, e in enumerate(self._ordered):
            if x <= e:
                self._ordered.insert(i, x)

    # @return nothing
    def pop(self):
        x =  self._s[-1]
        self._s = self._s[:-1]
        for i in self._ordered:
            if i == x:
                self._ordered.remove(x)
                break
        return x


    # @return an integer
    def top(self):
        return self._s[:-1]


    # @return an integer
    def getMin(self):
        if len(self._ordered) == 0:
            return None
        return self._ordered[-1]
