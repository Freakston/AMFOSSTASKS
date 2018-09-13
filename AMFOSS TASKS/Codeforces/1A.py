#!python3
import math
b=input()
n =int(b[0])
m =int(b[2])
a =int(b[4])
if (1 <= n <= 10**9):
        if (1 <= m <= 10**9):
            if (1 <= a <= 10**9):
                rows =math.ceil(n/a)
                column =math.ceil(m/a)
                final =rows*column
print(final)
