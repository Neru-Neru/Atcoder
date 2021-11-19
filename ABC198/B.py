n=input()
rn=n[::-1]
j=0
for i in range(len(rn)):
    if(n[j] != rn[i]):
        if(rn[i]!='0'):
            print('No')
            exit()
    else:
        j+=1
print('Yes')