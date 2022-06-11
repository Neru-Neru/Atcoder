r, c = map(int, input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
if r == 1:
    print(a[c-1])
else:
    print(b[c-1])