n=int(input())
a,b,c=map(int, input().split())
limit = 9999
ans = 10000000
for i in range(limit):
    for j in range(limit - i + 1):
        val = n - (a*i + b*j)
        near_ans = i + j + val // c
        if val < 0 or near_ans > 9999 or v % c != 0:
            continue
        ans = min(ans, near_ans)
print(ans)