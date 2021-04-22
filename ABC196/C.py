n=int(input())
n_copy=n
digit=0
while n_copy/10 > 0:
	digit+=1
	n_copy=n_copy//10
if digit%2 == 0:
	bot = int(n%(pow(10, digit//2)))
	top = n//(pow(10, digit//2))
	if top>bot:
		print(top-1)
	else:
		print(top)
else:
	print(pow(10, digit//2)-1)
