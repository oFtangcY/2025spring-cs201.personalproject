import sys
from collections import defaultdict

for line in sys.stdin:
    n = len(line)

    s = []
    res = defaultdict(lambda : ' ')

    for i in range(n):
        if line[i] == '(':
            s.append(i)
            res[i] = '$'
        elif line[i] == ')':
            if s:
                match = s.pop()
                res[match] = ' '
            else:
                res[i] = '?'

    print(line, end='')
    for i in range(n - 1):
        print(res[i], end='')
    print()
