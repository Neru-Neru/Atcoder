n=int(input())
digit=1
ans=0
while n-10**digit >= 0:
    digit+=1
i=1
while n >= 10**i-1:
    ans+=9*i*((i-1)//3)
    i+=1
ans+=(n-10*(digit-1))*(digit-1)//3
print(ans)