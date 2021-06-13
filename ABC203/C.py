n,k=map(int, input().split())
friends=[]
for i in range(n):
    a,b=map(int, input().split())
    friends.append([a, b])
friends.sort()
ans = 0
index = 0
while k > 0:
    ans += k
    next_k = 0
    while index < n and friends[index][0] <= ans:
        next_k += friends[index][1]
        index += 1
    k = next_k
print(ans) 