n=int(input())
aa=list(map(int, input().split()))
b=list(map(int, input().split()))
c=list(map(int, input().split()))
a=[0]*(10**5 + 10)
d=[0]*(10**5 + 10)
for i in aa:
    a[i] += 1
for i in c:
    d[b[i - 1]] += 1
cnt = 0
for i in range(10**5 + 10):
    cnt += a[i] * d[i]
print(cnt)