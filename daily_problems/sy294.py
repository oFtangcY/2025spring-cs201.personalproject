#pre-problem

n = int(input())
pop_list = list(map(int, input().split()))
s = []
j = 0

for i in range(1, n + 1):
    s.append(i)
    while s:
        if pop_list[j] == s[-1]:
            s.pop()
            j += 1
        else:
            break

    if j == n:
        print('Yes')
        exit()
    elif len(s) == 0:
        continue
    elif pop_list[j] < s[-1]:
        print('No')
        exit()
