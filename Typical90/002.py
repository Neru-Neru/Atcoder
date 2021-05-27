#Clear !Binary Loop
n=int(input())
if n%2 != 0:
    exit()
for i in range(2**n):
    ans=''
    nbr=0
    for j in range(n):
        if i&1:
            nbr+=1
            ans = ')' + ans
        else:
            if nbr > 0:
                nbr -= 1
                ans = '(' + ans
            else:
                break
        i = i>>1
        if j == n-1 and nbr == 0:
            print(ans)