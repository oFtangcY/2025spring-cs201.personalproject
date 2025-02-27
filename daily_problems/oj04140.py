#http://cs101.openjudge.cn/practice/04140/

def newton_method(f, f_prime, x0, tol=1e-9, max_iter=1000):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)

        if abs(fpx) < tol:
            raise ValueError("导数为零，无法继续迭代。")

        x_new = x - fx / fpx

        if abs(x_new - x) < tol:
            return x_new

        x = x_new

    raise ValueError("牛顿法未能在最大迭代次数内收敛。")


def f(x):
    return x ** 3 - 5 * x ** 2 + 10 * x - 80


def f_prime(x):
    return 3 * x ** 2 - 10 * x + 10


x0 = 5.0

try:
    root = newton_method(f, f_prime, x0)
    print(f"{root:.9f}")
except ValueError as e:
    print(e)
