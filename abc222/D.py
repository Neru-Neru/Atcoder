n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
cnt = 1
c_min = 0
for i in range(n):
    cnt *= (b[i]-a[i]+1)
    c_min = b[i]
print(cnt % 998244353)