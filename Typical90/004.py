## Timeout because of python
h,w = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]
w_s = [0]*h
h_s = [0]*w
for i in range(h):
    for j in range(w):
        w_s[i] += a[i][j]
        h_s[j] += a[i][j]
ans = []
for i in range(h):
    row = []
    for j in range(w):
        row.append(w_s[i] + h_s[j] - a[i][j])
    ans.append(row)
for a in ans:
    print(*a)