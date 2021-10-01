l = [0]*4
for i in range(4):
    s = input()
    if s == 'H':
        l[0]+=1
    elif s=='2B':
        l[1]+=1
    elif s=='3B':
        l[2]+=1
    else:
        l[3]+=1
for a in l:
    if a != 1:
        print('No')
        exit()
print('Yes')