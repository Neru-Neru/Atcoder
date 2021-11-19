def search(g):
    

n,m=map(int, input().split())
g = [[] for i in range(n)]
li = []
for i in range(m):
    ipt = list(map(int, input().split()))
    li.append(ipt)
li = sorted(li, key=lambda x: x[1])
while True:
    for l in li:
        x = 0
        while (x+l[0])%n not in g[x]:
            label = [0]*n
            g[x].append((x+l[0])%n)
            g[(x+l[0])%n].append(x)
            x += l[0]
            x = x % n
    print(g)
    break
print('Fin')