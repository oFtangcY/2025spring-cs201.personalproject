#http://cs101.openjudge.cn/2025sp_routine/04067/

while True:
    try:
        s = input()
        if s == s[::-1]:
            print('YES')
        else:
            print('NO')
    except EOFError:
        break
