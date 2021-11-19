n=int(input())
a=list(map(int, input().split()))
cnt = 0
for i in a:
    if i > 10:
        cnt += (i-10)
print(cnt)