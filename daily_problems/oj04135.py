#http://cs101.openjudge.cn/practice/04135

n ,m = map(int, input().split())
spend_list = [int(input()) for _ in range(n)]

def check(s):
    fajo_spend = 0
    months = 1
    for monthly_spend in spend_list:
        if fajo_spend + monthly_spend > s:
            months += 1
            if months > m:
                return False
            fajo_spend = monthly_spend
        else:
            fajo_spend += monthly_spend
    return True

lo, hi = max(spend_list), sum(spend_list) + 1
while lo < hi:
    mid = (lo + hi) // 2
    if check(mid):
        hi = mid
    else:
        lo = mid + 1

print(lo)
