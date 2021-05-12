str=input()
cnt=0
for i in range(9):
    if str[i]=='Z':
        if str[i+1]=='O':
            if str[i+2]=='N':
                if str[i+3]=='e':
                    cnt+=1
print(cnt)