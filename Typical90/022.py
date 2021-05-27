## Clear
import math

a,b,c=map(int, input().split())
r = math.gcd(a, math.gcd(b, c))
print(a//r + b//r + c//r - 3)