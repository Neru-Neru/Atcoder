n=int(input())
a=list(map(int, input().split()))
if n%2 == 0:
    bef = a[:n//2]
    aft = a[n//2:]
    aft.reverse()
else:
    bef = a[:n//2]
    aft = a[n//2 + 1:]
    aft.reverse()
for i in range(len(bef)):
    if bef[i] != aft[i]:
        hamming