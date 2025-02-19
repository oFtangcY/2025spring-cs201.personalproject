#pre-problem

n, m = map(int, input().split())
nums = list(map(int, input().split()))

for _ in range(m):
    op, x = input().split()
    x = int(x)

    if op == 'C':
        for i in range(n):
            nums[i] = (nums[i] + x) % 65535

    elif op == 'Q':
        res = 0

        for i in range(n):
            bin_num = str(bin(nums[i]))[2:]

            if x < len(bin_num) and bin_num[- x - 1] == '1':
                res += 1

        print(res)
