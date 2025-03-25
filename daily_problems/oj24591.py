oprators = {'+':1, '-':1, '*':2, '/':2}

def infix_to_postfix(expression):
    s = []
    postfix = []
    num = ''

    for char in expression:
        if char.isdigit() or char == '.':
            num += char
        else:
            if num:
                postfix.append(num)
                num = ''
            if char in '+-*/':
                while s and s[-1] in '+-*/' and oprators[s[-1]] >= oprators[char]:
                    postfix.append(s.pop())
                s.append(char)
            elif char == '(':
                s.append(char)
            elif char == ')':
                while s and s[-1] != '(':
                    postfix.append(s.pop())
                s.pop()

    if num:
        postfix.append(num)
    while s:
        postfix.append(s.pop())

    return postfix

n = int(input())
for _ in range(n):
    expr = input()
    print(' '.join(map(str, infix_to_postfix(expr))))


