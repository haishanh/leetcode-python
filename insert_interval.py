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
        start = newInterval.start
        end   = newInterval.end
        new = []
        tmp_start = ''
        for i, e in enumerate(intervals):
            if end < e.start:
                new.append(newInterval)
                if tmp_start:
                    new.append(Interval(tmp_start, end))
                new.append(e)
                break
            else: # end >= e.start
                if end <= e.end:
                    if tmp_start:
                        new.append(tmp_start, e.end)
                        break
                    if start < e.start:
                        new.append(Interval(start, e.end))
                        break
                    else:
                        new.append(e)
                        break
                else:
                    tmp_start = min(e.start, start)
                    continue
        for e in intervals[i:]:
            new.append(e)
        return new

# TODO
class Solution2:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        start =  newInterval.start
        end = newInterval.end
        overlap = []
        # no overlapping case 1
        if end < intervals[0].start:
            return [newInterval] + intervals
        # no overlapping case 2
        if start > intervals[-1].end:
            return intervals + [newInterval]
        for i, e in enumerate(intervals):
            if (start <= e.start and end >= e.end) or\
               (start >= e.start and end <= e.end) or\
               (start <= e.end and end >= e.end) or\
               (start <= e.start and end>= e.start):
                overlap.append(i)
        if overlap:
            tmp_inter = Interval(min(intervals[overlap[0]].start, start), max(intervals[overlap[-1]].end, end))
            return intervals[:overlap[0]] + [tmp_inter] + intervals[overlap[-1]+1:]
        # no overlapping case 3
        else:
            for i, e in enumerate(intervals):
                if end < e.start:
                    break
            return intervals[:i] + [newInterval] + intervals[i:]


def test():
    s = Solution2()
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

if __name__ == '__main__':
    test()
