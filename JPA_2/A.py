import math

x, y, z=map(int, input().split())
taka = y/x
price = taka*z
if price.is_integer():
    print(int(price-1))
else:
    print(math.floor(price))