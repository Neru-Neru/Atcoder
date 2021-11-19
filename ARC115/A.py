n,m=map(int, input().split())
s=[]
for _ in range(n):
	tmp=int(input(), 2)
	s.append(tmp)
ans=100000000
for bit in range(pow(2, m)):
	dic={}
	for j in s:
		x=0
		x=bin(j^bit).count("1")
		if x in dic:
			dic[x]+=1
		else:
			dic[x]=1
	cnt=0
	copy=0
	for d in dic.values():
		if d==1:
			cnt+=1
		else:
			copy+=d
	pre_ans = max(cnt*copy, cnt)
	print(pre_ans)
	ans=min(ans, pre_ans)
print(ans)