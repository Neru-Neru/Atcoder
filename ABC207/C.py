n=int(input())
left = 0
right = pow(10, 9)
li=[]
for i in range(n):
    t,l,r=map(int, input().split())
    li.append([t,l,r])
cnt = 0
for i in range(n):
    l_i = li[i]
    for j in range(i+1, n):
        l_j = li[j]
        if (l_i[0]==1 or l_i[0]==2):
            left_i = l_i[1]
        else:
            left_i = l_i[1]+0.5
        if (l_j[0]==1 or l_j[0]==2):
            left_j = l_j[1]
        else:
            left_j = l_j[1]+0.5
        if (l_i[0]==1 or l_i[0]==3):
            right_i = l_i[2]
        else:
            right_i = l_i[2]-0.5
        if (l_j[0]==1 or l_j[0]==3):
            right_j = l_j[2]
        else:
            right_j = l_j[2]-0.5
        if (left_j <= left_i and left_i <= right_j)or(left_j <= right_i and right_i <= right_j)or(left_i <= left_j and left_j <= right_i)or(left_i <= right_j and right_j <= right_i):
            cnt += 1
print(cnt)
