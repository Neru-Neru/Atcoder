#Clear
n,k=map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

dis=0
for i in range(n):
    dis += abs(a[i]-b[i])
if (k - dis)%2 == 0 and dis <= k:
    print('Yes')
else:
    print('No')