import math

a,b,c,d=map(int,input().split())
if c*d-b == 0:
    print(-1)
else:
    t = a/(c*d-b)
    if t<0:
        print(-1)
    else:
        print(math.ceil(t))