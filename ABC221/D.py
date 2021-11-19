login=[0]*(10**9+3)
logout=[0]*(10**9+3)
n=int(input())
day=[0]*(n+1)
for i in range(n):
    a, b=map(int, input().split())
    login[a]+=1
    logout[a+b-1]+=1
for i in range(len(login)):
    day[login[i]-logout[i]] += 1
print(day)