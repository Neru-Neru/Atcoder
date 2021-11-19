## Clear
n=int(input())
score=[[0 for i in range(2)] for j in range(n+1)]
ans=[]
for i in range(n+1):
    if i == 0:
        continue
    c, p = map(int, input().split())
    prev = score[i-1]
    score[i][0] += prev[0]
    score[i][1] += prev[1]
    score[i][c-1] += p
q=int(input())
for j in range(q):
    l, r = map(int, input().split())
    ans.append([score[r][0] - score[l-1][0], score[r][1] - score[l-1][1]])
for a in ans:
    print(*a)