import math

t = int(input())
l, x, y = map(int, input().split())
q = int(input())
for i in range(q):
    e = int(input())
    cx = 0
    cy = -1 * l * math.sin(2*math.pi*e/t) / 2
    cz = l/2 - l * math.cos(2*math.pi*e/t) / 2
    print(math.degrees(math.atan2(cz, math.sqrt(x**2 + (y - cy)**2))))