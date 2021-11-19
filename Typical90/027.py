## Clear
from collections import defaultdict
n=int(input())
s=defaultdict(int)
for i in range(n):
    tmp = input()
    if s[tmp] == 0:
        s[tmp] += 1
        print(i+1)
