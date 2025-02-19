#pre-problem

s = []
n = int(input())

for _ in range(n):
    order = input()

    if order == 'pop':
        if s:
            print(s.pop())
        else:
            print(-1)
    else:
        order = order.split()
        s.append(int(order[1]))
