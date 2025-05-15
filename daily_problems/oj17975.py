# http://cs101.openjudge.cn/2025sp_routine/17975/
# Quadratic Probing in Hashing

import sys
input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
keys = [int(i) for i in data[index:index+n]]

def quadratic_prob(t):
    return (-1) ** ((t + 1) % 2) * ((t + 1) // 2) ** 2

def hash(table, keys, m):
    res = []
    for key in keys:
        hv = key % m

        if table[hv] == -1 or table[hv] == key: # there might be repeat numbers
            table[hv] = key
        else:
            for j in range(1, m + 1):
                idx = (key + quadratic_prob(j)) % m
                if idx < m and (table[idx] == -1 or table[hv] == key):
                    table[idx] = key
                    hv = idx
                    break
        res.append(hv)

    return res

table = [-1] * m
print(' '.join(map(str, hash(table, keys, m))))