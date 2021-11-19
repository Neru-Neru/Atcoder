import math

r, x, y=map(int, input().split())
dis2=math.sqrt(x*x+y*y)
ans2=0
while True:
    if (ans2*r >= dis2):
        break
    ans2+=1
print(math.ceil(ans2))