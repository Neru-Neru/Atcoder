a,b=map(int, input().split())
ans = a/3+2*b/3
if ans.is_integer():
    print(int(ans))
else:
    print(ans)