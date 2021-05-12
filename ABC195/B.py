import math
a,b,w=map(int, input().split())
w=w*1000
l=math.ceil(w/b)
u=math.floor(w/a)
if l-u <= 0:
    print(l,u)
else:
    print('UNSATISFIABLE')