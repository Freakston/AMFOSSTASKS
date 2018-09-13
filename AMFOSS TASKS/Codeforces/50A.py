#!python3
n,m=list(map(int, input().split()))
import math

b=n*m

if (b%2 == 0):
   print(n*m/2)

else:
    a=math.ceil(int(b/2))
    print(a)
