n=int(input())
s=list(input())
q=int(input())
flg = 0
for i in range(q):
    t,a,b = map(int, input().split())
    if t == 1:
        if flg == 0:
            tmp = s[a-1]
            s[a-1] = s[b-1]
            s[b-1] = tmp
        else:
            if a < n:
                a = n + a
            else:
                a = a - n
            if b < n:
                b = n + b
            else:
                b = b - n
            tmp = s[a-1]
            s[a-1] = s[b-1]
            s[b-1] = tmp
    else:
        flg ^= 1
if flg == 1:
    s = s[n:]+s[:n]
ans = ''.join(s)
print(ans)

