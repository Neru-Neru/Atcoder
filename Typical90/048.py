n, k =map(int, input().split())
score = []
for _ in range(n):
    ca, cb = map(int, input().split())
    score.append(ca-cb)
    score.append(cb)
score.sort(reverse=True)
ans = 0
for i in range(k):
    ans += score[i]
print(ans)
