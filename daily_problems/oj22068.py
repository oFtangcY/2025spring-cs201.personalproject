#http://cs101.openjudge.cn/practice/22068/

def is_legal(output, origin):
    if len(origin) != len(output):
        return False

    string = list(origin)
    stack = []
    
    for char in output:
        while (not stack or stack[-1] != char) and string:
            stack.append(string.pop(0))

        if not stack or stack[-1]!= char:
            return False

        stack.pop()

    return True


x = input().strip()
while True:
    try:
        output = input().strip()
        if is_legal(output, x):
            print('YES')
        else:
            print('NO')
    except EOFError:
        break