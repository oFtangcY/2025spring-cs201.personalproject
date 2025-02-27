#http://cs101.openjudge.cn/practice/19942/

m, n, p, q = map(int, input().split())
ori_mat = []
for _ in range(m):
    ori_mat.append(list(map(int, input().split())))
ker_mat = []
for _ in range(p):
    ker_mat.append(list(map(int, input().split())))

out_mat = [[] for _ in range(m + 1 - p)]
for i in range(m + 1 - p):
    for j in range(n + 1 - q):
        ele_out_mat = 0
        for k in range(p):
            for l in range(q):
                ele_out_mat += ker_mat[k][l] * ori_mat[k + i][l + j]
        out_mat[i].append(ele_out_mat)

for i in range(m + 1 - p):
    print(' '.join(map(str, out_mat[i])))
