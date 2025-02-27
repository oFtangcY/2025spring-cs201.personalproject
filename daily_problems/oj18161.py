#http://cs101.openjudge.cn/practice/18161/

def input_matrix(r, c):
    mat = []
    for _ in range(r):
        mat.append(list(map(int, input().split())))

    return mat


r_a, c_a = map(int, input().split())
mat_a = input_matrix(r_a, c_a)
r_b, c_b = map(int, input().split())
mat_b = input_matrix(r_b, c_b)
r_c, c_c = map(int, input().split())
mat_c = input_matrix(r_c, c_c)

if r_a != r_c or c_a != r_b or c_b != c_c:
    print('Error!')
    exit()

product_a_b = [[] for _ in range(r_a)]
for i in range(r_a):
    for j in range(c_b):
        product_a_b[i].append(sum(mat_a[i][k] * mat_b[k][j] for k in range(c_a)))

sum_ab_c = [[] for _ in range(r_a)]
for i in range(r_a):
    for j in range(c_c):
        sum_ab_c[i].append(product_a_b[i][j] + mat_c[i][j])

for i in range(r_a):
    print(' '.join(map(str, sum_ab_c[i])))
