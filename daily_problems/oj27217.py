#http://cs101.openjudge.cn/2025sp_routine/27217/

#this program is TLE
'''
import sys
sys.setrecursionlimit(10000)

def generate_output(stack, in_stack):
    out = 0
    if len(stack) == 0 and len(in_stack) == 0:
        return 1

    if len(stack) > 0:
        out += generate_output(stack[:-1], in_stack)
    if len(in_stack) > 0:
        out += generate_output(stack + [in_stack[0]], in_stack[1:])

    return out


n = int(input())
in_stack = list(range(n))
print(generate_output([], in_stack))
'''

#the following program uses the formula for Catalan numbers
#C(n) = C(2n,n)/(n+1)
from math import factorial

n = int(input())

print(factorial(2 * n) // (factorial(n) ** 2 * (n + 1)))