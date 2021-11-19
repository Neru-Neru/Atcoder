h,w,x,y=map(int, input().split())
x -= 1
y -= 1
s=[]
for _ in range(h):
    s.append(input())
cnt = 0
i = y
while i >= 0 and s[x][i] == '.':
    cnt += 1
    i -= 1
i = y
while i < w and s[x][i] == '.':
    cnt += 1
    i += 1
j = x
while j >= 0 and s[j][y] == '.':
    cnt += 1
    j -= 1
j = x
while j < h and s[j][y] == '.':
    cnt += 1
    j += 1
print(cnt-3)