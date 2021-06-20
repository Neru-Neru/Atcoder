def binary_search(array, item):
   head = 0
   tail = len(array) - 1

   while head <= tail:
       center = (head + tail) // 2
       if array[center] == item:
           return center
       elif array[center] < item:
           head = center + 1
       else:
           tail = center - 1
   return None
   
n,q=map(int, input().split())
a=list(map(int, input().split()))
a.sort()
maxim = max(a)
num = []
top = a.pop(0)
index = 0
for i in range(maxim + 1):
    if i != top:
        index += 1
    else:
        if len(a) != 0:
            top = a.pop(0)
    num.append(index)
m = max(num)
for i in range(q):
    k = int(input())
    if k < m:
        res = binary_search(num, k)
        print(res+1)
    else:
        print(len(num)+k-m)