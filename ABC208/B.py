coin=[3628800,362880,40320,5040,720,120,24,6,2,1]
p=int(input())
num = 0
for c in coin:
    while p >= c:
        div = p//c
        p = p%c
        num += div
    if p == 0:
        break
print(num)