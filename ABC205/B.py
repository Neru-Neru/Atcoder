n=int(input())
a=list(map(int, input().split()))
num=[False]*n
for i in a:
    if num[i-1] == False:
        num[i-1] = True
for i in num:
    if i == False:
        print('No')
        exit()
print('Yes')