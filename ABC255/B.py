from math import sqrt

n, k = map(int, input().split())
a = list(map(int, input().split()))
a_dict = {}
for aa in a:
    a_dict[aa-1] = 1
light = []
human = []
for i in range(n):
    cx, cy = map(int, input().split())
    if i in a_dict:
        light.append([cx, cy])
    else:
        human.append([cx, cy])
ans = 0
for h in human:
    dist = 10000000000000000000000
    for l in light:
        c_dist = (l[0]-h[0])**2 + (l[1]-h[1])**2
        dist = min(dist, c_dist)
    ans = max(ans, dist)
print(sqrt(ans))
