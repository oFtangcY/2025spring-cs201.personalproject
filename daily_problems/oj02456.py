#http://cs101.openjudge.cn/2025sp_routine/02456/

n, c = map(int, input().split())
x = sorted([int(input()) for i in range(n)])
min_d = 10 ** 9
for i in range(1, n):
    min_d = min(x[i] - x[i - 1], min_d)

def check(d_min):
    i, last = 0, 0
    for _ in range(c - 1):
        while x[i] - x[last] < d_min:
            i += 1
            if i == n:
                return False
        last = i
    return True

lo, hi = min_d, x[-1] - x[0]
while lo < hi:
    mid = (lo + hi) // 2
    if check(mid):
        lo = mid + 1
        ans = mid
    else:
        hi = mid

print(ans)
