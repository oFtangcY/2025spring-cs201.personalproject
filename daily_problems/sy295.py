def generate_sequences(stack, in_stack, out_stack, output):
    if len(in_stack) == 0 and len(stack) == 0:
        output.append(out_stack)

    if len(stack) > 0:
        generate_sequences(stack[:-1], in_stack, out_stack + [stack[-1]], output)

    if len(in_stack) > 0:
        generate_sequences(stack + [in_stack[0]], in_stack[1:], out_stack, output)


n = int(input())
in_stack = list(range(1, n + 1))
output = []

generate_sequences([], in_stack, [], output)
output.sort()

for sequence in output:
    print(' '.join(map(str, sequence)))
