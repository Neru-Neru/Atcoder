n=int(input())
a=[]
for i in range(n):
  s,t=input().split()
  t=int(t)
  a.append([t,s])
a.sort(reverse=True)
print(a[1][1])