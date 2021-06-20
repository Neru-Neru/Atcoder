n=int(input())
a=list(map(int, input().split()))
dic = {}
cnt = 0
for i in a:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
for k, v in dic.items():
    cnt += (n - v)*v
print(cnt//2)