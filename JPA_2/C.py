a,b = map(int, input().split())
m = szsssszz1
ans=1
i = a
table = []
while i * i <= b:
    if n%i == 0:
        table.append(i)
        table.append(n//i)
    i += 1
table = list(set(table))
