#!/usr/bin/env python

from __future__ import print_function


# TODO Time exceeded and verbose coding
# use recursion for parentheses substring
class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        before = ''
        after = ''
        i = 0
        pre_sign = ''
        parentheses_sub_string = ''
        while i < len(s):
            while i < len(s) and s[i] not in '+ -()':
                if pre_sign:
                    after += s[i]
                else:
                    before += s[i]
                i += 1
            # caculate begin
            if pre_sign == '+' and after:
                before = str(int(before) + int(after))
                after = ''
                pre_sign = ''
            elif pre_sign == '-' and after:
                before = str(int(before) - int(after))
                after = ''
                pre_sign = ''
            # caculate done
            if i < len(s):
                if s[i] in '+-':
                    pre_sign = s[i]
                    i += 1
                elif s[i] == ' ':
                    i += 1
                elif s[i] == '(':
                    i += 1
                    left_parenthese_count = 1
                    right_parenthese_count = 0
                    while i < len(s):
                        if s[i] == '(':
                            left_parenthese_count += 1
                        if s[i] == ')':
                            right_parenthese_count += 1
                            if left_parenthese_count == right_parenthese_count:
                                i += 1
                                break
                        parentheses_sub_string += s[i]
                        i += 1
                    if pre_sign:
                        after = str(self.calculate(parentheses_sub_string))
                    else:
                        before = str(self.calculate(parentheses_sub_string))
                    parentheses_sub_string = ''
                    # i += 1 # ')'
        if after:
            if pre_sign == '+':
                return int(before) + int(after)
            if pre_sign == '-':
                return int(before) - int(after)
        return int(before)



class Solution2:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        numstack = []
        opstack = []
        i = len(s) -1
        while i > -1:
            if s[i] in '0123456789':
                j  = i
                while  i > -1 and s[i] in '0123456789':
                    i -= 1
                i += 1
                numstack.append(int(s[i:j+1]))
            else:
                if s[i] in ')+-':
                    opstack.append(s[i])
                if s[i] == '(':
                    while opstack[-1] != ')':
                        if opstack.pop() == '+':
                            numstack.append(numstack.pop()+numstack.pop())
                        else:
                            numstack.append(numstack.pop()-numstack.pop())
                    opstack.pop()
            i -= 1
        while opstack:
            if opstack.pop()=='+':
                numstack.append(numstack.pop()+numstack.pop())
            else:
                numstack.append(numstack.pop()-numstack.pop())
        return numstack[-1]

def test():
    s = Solution2()
    expression = ' 1 + 2'
    res = s.calculate(expression)
    print('%s = %d' % (expression, res))
    assert 3 == res

    expression = ' 22 + 12'
    res = s.calculate(expression)
    print('%s = %d' % (expression, res))
    assert 34 == res

    expression = ' 2- 1 -2'
    res = s.calculate(expression)
    print('%s = %d' % (expression, res))
    assert -1 == res

    expression = '(3) + 2'
    res = s.calculate(expression)
    print('%s = %d' % (expression, res))
    assert 5 == res

    expression = '1+2'
    res = s.calculate(expression)
    print('%s = %d' % (expression, res))
    assert 3 == res

    expression = '1 + (4+5)'
    res = s.calculate(expression)
    print('%s = %d' % (expression, res))
    assert 10 == res

    expression = '(1 +(4+ 5+2)-3)+(6+8)'
    res = s.calculate(expression)
    print('%s = %d' % (expression, res))
    assert 23 == res

    print('Test passed!')


if __name__ == '__main__':
    test()
