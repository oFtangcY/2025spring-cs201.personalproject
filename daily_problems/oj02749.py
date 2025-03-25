#http://cs101.openjudge.cn/2025sp_routine/02749/

def devide_num(num, min_factor):
    if num == 1:
        return 1

    devide_ways = 0
    for factor in range(min_factor, num + 1):
        if num % factor == 0:
            devide_ways += devide_num(num // factor, factor)

    return devide_ways


n = int(input())
for _ in range(n):
    num = int(input())
    print(devide_num(num, 2))