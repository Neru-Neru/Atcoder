s=input()
if s[0]==s[1] and s[1] == s[2] and s[2] == s[3]:
    print('Weak')
    exit()
for i in range(3):
    if int(s[i+1]) != int(s[i])+1:
        if s[i] != '9' or s[i+1] != '0':
            print('Strong')
            exit()
print('Weak')