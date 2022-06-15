n=int(input())
a=list(map(int, input().split()))
b = sorted(a, reverse=True)
for i in range(len(a)):
    if a[i] == b[1]:
        print(i+1)
        break