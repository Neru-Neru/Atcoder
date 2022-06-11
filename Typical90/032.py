import itertools

n = int(input())
a = []
for _ in range(n):
    aa = list(map(int, input().split()))
    a.append(aa)
m = int(input())
relation = [[False]*n for i in range(n) ]
for _ in range(m):
    x, y = map(int, input().split())
    relation[x-1][y-1] = True
    relation[y-1][x-1] = True
ans = -1
for it in itertools.permutations(range(n)):
    ctime = 0
    for i in range(n-1):
        pre = it[i]
        aft = it[i+1]
        if relation[pre][aft]:
            break
        ctime += a[pre][i]
        if i == n-2:
            ctime += a[aft][i+1]
            if ans == -1:
                ans = ctime
            else:
                ans = min(ans, ctime)
print(ans)