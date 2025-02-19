from collections import defaultdict

n = int(input())
big_models = defaultdict(list)
for _ in range(n):
    name, para = input().split('-')
    if para[-1] == 'B':
        para = (float(para[:-1]) * 1000, para)
    else:
        para = (float(para[:-1]), para)

    big_models[name].append(para)

for model in sorted(big_models.keys()):
    big_models[model].sort()
    print(model + ':', end = ' ')

    for i in range(len(big_models[model])):
        para = big_models[model][i][1]
        print(para, end='')
        if i < len(big_models[model]) - 1:
            print(',', end=' ')
        else:
            print()
