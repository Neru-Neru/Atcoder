h,w,a,b=map(int, input().split())
li=[]
map_l=[[0]*(w+1)]*(h+1)
for _ in range(a):
	li.append([2,1])
for _ in range(b):
	li.append([1,1])
for i in range(w):
	for j in range(h):
		