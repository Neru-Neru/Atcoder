x, a, d, n = map(int, input().split())
left = min(a, a + (n-1)*d)
right = max(a, a + (n-1)*d)
if d == 0:
    print(abs(a - x))
elif x < left:
    print(abs(left - x))
elif right < x:
    print(abs(x - right))
else:
    tmp = abs(x - a) % abs(d)
    print(min(tmp, abs(abs(d) - tmp)))