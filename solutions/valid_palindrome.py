#!/usr/bin/env python

#.Try not to use builtin sring method, isalpha(), isdigit(), lower(), upper()
#.Performance of course not good as one use these buildtins
class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        def is_alphanumeric(c):
            if 'a' <= c <= 'z' or \
               'A' <= c <= 'Z' or \
               '0' <= c <= '9':
                return True
        def is_same(x, y):
            ''' alphanumeric validation not needed as it have done before '''
            if x == y:
                return True
            x = ord(x)
            y = ord(y)
            if x < y and x + 32 == y:
                return True
            if x > y and y + 32 == x:
                return True
        if len(s) <= 1:
            return True
        i = 0
        j = len(s) - 1
        while i <= j:
            while not is_alphanumeric(s[i]):
                i += 1
                if i >= j:
                    return True
            while not is_alphanumeric(s[j]):
                j -= 1
                if i >= j:
                    return True
            if not is_same(s[i], s[j]):
                return False
            i += 1
            j -= 1
        return True

def test():
    s = Solution()
    assert True == s.isPalindrome("A man, a plan, a canal: Panama")
    assert False == s.isPalindrome("race a car")
    print('Test passed')


if __name__ == '__main__':
    test()
