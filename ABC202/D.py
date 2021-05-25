import math

a,b,k=map(int, input().split())
ans = ''
len = a + b
floor = 0
for i in range(len):
    if a == 0 or b == 0:
        break
    if k > floor + math.factorial(a + b - 1)//(math.factorial(a - 1)*math.factorial(b)):
        ans += 'b'
        floor += math.factorial(a + b - 1)//(math.factorial(a - 1)*math.factorial(b))
        b -= 1
    else:
        ans += 'a'
        a -= 1
for i in range(a):
    ans += 'a'
for i in range(b):
    ans += 'b'
print(ans)