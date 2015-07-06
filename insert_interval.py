#!/usr/bin/env python
from __future__ import print_function

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        start =  newInterval.start
        end = newInterval.end
        overlap = []
        # no overlapping case 1 | [[5,6],[7,8]] [2,4]
        if end < intervals[0].start:
            return [newInterval] + intervals
        # no overlapping case 2 | [[2,3],[5,7]] [9-11]
        if start > intervals[-1].end:
            return intervals + [newInterval]
        for i, e in enumerate(intervals):
            if (start <= e.start and end >= e.end) or \
               (start >= e.start and end <= e.end) or \
               (start <= e.end and end >= e.end) or \
               (start <= e.start and end>= e.start):
                overlap.append(i)
        if overlap:
            tmp_inter = Interval(min(intervals[overlap[0]].start, start), max(intervals[overlap[-1]].end, end))
            return intervals[:overlap[0]] + [tmp_inter] + intervals[overlap[-1]+1:]
        # no overlapping case 3 | [[2,4],[10,20]] [5,7]
        else:
            for i, e in enumerate(intervals):
                if end < e.start:
                    break
            return intervals[:i] + [newInterval] + intervals[i:]


def test():
    s = Solution()
    l = [[1, 3], [6, 9]]
    intervals = []
    for i in l:
        inter = Interval()
        inter.start = i[0]
        inter.end   = i[1]
        intervals.append(inter)
    new_inter = Interval()
    new_inter.start = 2
    new_inter.end = 5
    res = s.insert(intervals, new_inter)
    for i in res:
        print(i.start, i.end)
    print('-' * 20)
    intervals = []
    new_inter.start = 5
    new_inter.end = 7
    res = s.insert(intervals, new_inter)
    for i in res:
        print(i.start, i.end)

if __name__ == '__main__':
    test()
