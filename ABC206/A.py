import math

n=int(input())
p = math.floor(1.08 * n)
if p < 206:
    print('Yay!')
elif p == 206:
    print('so-so')
else:
    print(':(')