#!/usr/bin/env python

class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
    # @param {integer} numRows
    # @return {integer[][]}
        def gen_one(n):
            tmp = [0] + n + [0]
            for i in range(len(tmp) - 1):
                tmp[i] += tmp[i+1]
            return tmp[:-1]
        tmp = [1]
        for i in range(rowIndex):
            tmp = gen_one(tmp)
        return tmp

    def generate(self, numRows):
        def gen_one(n):
            tmp = [0] + n + [0]
            for i in range(len(tmp) - 1):
                tmp[i] += tmp[i+1]
            return tmp[:-1]
        if numRows == 0:
            return []
        res = []
        tmp = [1]
        for i in range(numRows):
            res.append(tmp)
            tmp = gen_one(tmp)
        return res


def test():
    s = Solution()
    assert [1, 1] == s.getRow(1)
    assert [1, 4, 6, 4, 1] == s.getRow(4)
    assert [1, 9, 36, 84, 126, 126, 84, 36, 9, 1] == s.getRow(9)
    print('Test passed')


if __name__ == '__main__':
    test()
