mid_suffix_expression = input().split()

while len(mid_suffix_expression) > 1:
    mid_suffix_expression = [mid_suffix_expression[0] + ' ' + mid_suffix_expression[2] + ' ' + mid_suffix_expression[1]] + mid_suffix_expression[3:]

print(mid_suffix_expression[0])
