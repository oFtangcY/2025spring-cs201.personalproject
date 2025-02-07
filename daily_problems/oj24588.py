def cal_poland_expression(expression):
    current = []
    for dig in expression:
        if dig == '+':
            current[-2:] = [current[-2] + current[-1]]
        elif dig == '-':
            current[-2:] = [current[-2] - current[-1]]
        elif dig == '*':
            current[-2:] = [current[-2] * current[-1]]
        elif dig == '/':
            current[-2:] = [current[-2] / current[-1]]
        else:
            current.append(float(dig))

    return current[0]


n = int(input())
for _ in range(n):
    poland_expression = input().split()
    res = cal_poland_expression(poland_expression)
    print('{:.2f}'.format(res))
