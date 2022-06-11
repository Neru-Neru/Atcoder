n = int(input())
ia = list(map(int, input().split()))
ib = list(map(int, input().split()))
ic = list(map(int, input().split()))
a = [0]*46
b = [0]*46
c = [0]*46
for i in range(n):
    a[ia[i] % 46] += 1
    b[ib[i] % 46] += 1
    c[ic[i] % 46] += 1

ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + j + k) % 46 == 0:
                ans += a[i]*b[j]*c[k]
print(ans)