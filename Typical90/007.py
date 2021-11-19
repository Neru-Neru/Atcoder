## Clear !Using Binry Search
import bisect

n=int(input())
a=list(map(int, input().split()))
a.sort()
q=int(input())
for _ in range(q):
    i = int(input())
    pos = bisect.bisect(a, i)
    if pos == 0:
        print(a[0] - i)
    elif pos == n:
        print(i - a[n-1])
    else:
        print(min(a[pos] - i, i - a[pos-1]))