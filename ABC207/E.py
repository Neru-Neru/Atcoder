def method(i, j, a):
    if i == n:
        print('Yes')
        return True
    s = a[i]
    while s%(j) != 0:
        i+=1
        if i == n:
            print('No')
            return False
        s += a[i]
    if method(i+1, j+1, a):
        return True

n=int(input())
a=list(map(int, input().split()))
s = 0
cnt = 0
for i in range(n):
    s += a[i]
    if method(i+1, 2, a):
        cnt += 1
print(cnt%(pow(10,9)+7))
