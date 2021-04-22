from itertools import permutations
s1=input()
s2=input()
s3=input()
s=s1+s2+s3
i=0
str=[]
while True:
    flg=1
    for s in str:
        if s==s[i]:
            flg=0
            break
    if i < 9:
        print('UNSOLVABLE')
        exit()
    if flg==1:
        str[i] = s[i]
        i+=1

for s_list in permutations(str):
    i=0
    for
    send = c[0]*1000 + c[1]*100 + c[2]*10 + c[3]
    more = c[4]*1000 + c[5]*100 + c[6]*10 + c[1]
    money = c[4]*10000 + c[5]*1000 + c[2]*100 + c[1]*10 + c[7]

if (send + more) == money and 10000 < money:
    print (c[0],c[1],c[2],c[3])
    print (c[4],c[5],c[6],c[1])
    print (c[4],c[5],c[2],c[1],c[7])