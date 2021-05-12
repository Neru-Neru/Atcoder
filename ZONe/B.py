n,ud,uh=map(int, input().split())
m=0.0
for i in range(n):
    d,h=map(int,input().split())
    katamuki = (uh-h)/(ud-d)
    if uh-(katamuki*ud) > m:
        m = uh-(katamuki*ud)
print(m)
