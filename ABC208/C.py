n,k=map(int,input().split())
a=list(map(int, input().split()))
b={}
for i in a:
    b[i] = 0
a_sort = sorted(a)
every1_snack = k//n
kdash = k % n
for j in range(kdash):
    b[a_sort[j]]+=1
for i in a:
    print(b[i] + every1_snack)