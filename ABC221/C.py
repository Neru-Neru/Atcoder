n=sorted(input())
a=0
b=0
last = 0
zeros = 0
for i in n:
    if n[0] != '0':
        break
    n.pop(0)
    zeros+=1
if len(n) % 2 != 0:
    last += int(n.pop(0))
for i in range(len(n)//2):
    a+=int(n[2*i]) * 10**(i)
    b+=int(n[2*i+1]) * 10**(i)
if last > 0:
    a=a*10+last
print(a*b*(10**zeros))