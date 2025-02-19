#pre-problem
#oct(_number)

def oct(num_10):
    num_8 = ''
    while num_10:
        num_8 = str(num_10 % 8) + num_8
        num_10 //= 8

    return num_8

print(oct(int(input())))
