S = int(input())
h = S // 3600
m = S % 3600 // 60
s = S % 60
print('{}:{}:{}'.format(h, m, s))