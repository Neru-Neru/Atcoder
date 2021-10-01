n,k=map(int, input().split())
c=list(map(int, input().split()))
d = {}
candy=[]
if n == k:
    for i in c:
        if not i in d:
            d[i] = 1
        else:
            d[i] += 1
    print(len(d))
else:
    for i in range(n):
        if i > k - 1:
            prev = c[i-k]
            candy.append(len(d))
            if d[prev] == 1:
                d.pop(prev)
            else:
                d[prev] -= 1
        if not c[i] in d:
            d[c[i]] = 1
        else:
            d[c[i]] += 1
    candy.append(len(d))
    print(max(candy))