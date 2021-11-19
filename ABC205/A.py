a,b=map(int, input().split())
kcal = a*(b/100)
if kcal.is_integer():
    print(int(kcal))
else:
    print(kcal)