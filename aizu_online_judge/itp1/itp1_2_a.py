a, b = map(int, input().split())
op = '<' if a < b else '>' if a > b else '=='
print('a {} b'.format(op))