#!/usr/bin/env python
# runtime: 1440 ms


class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        is_prime = [1] * n
        if n >= 2:
            is_prime[0] = 0
            is_prime[1] = 0
        else:
            return 0
        i = 2
        while True:
            j = i * i
            if j >= n:
                break
            if is_prime[i] == 0:
                i += 1
                continue
            while True:
                if j >= n:
                    break
                is_prime[j] = 0
                j += i
            i += 1
        count = reduce(lambda x, y: x+y, is_prime)
        return count


def test():
    s = Solution()
    assert 0 == s.countPrimes(0)
    assert 0 == s.countPrimes(1)
    assert 0 == s.countPrimes(2)
    assert 1 == s.countPrimes(3)
    assert 2 == s.countPrimes(4)
    assert 4 == s.countPrimes(10)
    assert 30 == s.countPrimes(120)
    assert 168 == s.countPrimes(1000)
    print('Test Passed!')

if __name__ == '__main__':
    test()
