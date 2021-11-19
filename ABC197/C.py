n=int(input())
a=list(map(int, input().split()))
m = 100000
for i in range(n-1):
    or_num = 0
    xor_num = 0
    for j in range(n+1):
        if j < n:
            or_num |= a[j]
            print(or_num)
        if (i >> j) & 1 or j == n:
            xor_num ^= or_num
            or_num = 0
        m = min(m, xor_num)
print(m)
