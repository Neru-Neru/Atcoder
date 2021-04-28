n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
dic={}
for i in range(n):
    start = a[i]
    end = b[i]
    while start <= end:
        if dic.get(start) != None:
            dic[start] += 1
        else:
            dic[start] = 1
        start += 1
ans = 0
for k, v in dic.items():
    if v == n:
        ans += 1
print(ans)