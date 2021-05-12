n=int(input())
a=list(map(int, input().split()))
li=[0]*200
ans=0
for i in a:
    li[i%200] += 1
for i in range(200):
    ans += (li[i]*(li[i]-1))//2
print(ans)