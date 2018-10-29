#!python3
import math
n,m,a =map(int, (input().split(" ")))

if (1 <= n <= 10**9):
        if (1 <= m <= 10**9):
            if (1 <= a <= 10**9):
                rows =math.ceil(n/a)
                column = math.ceil(m/a)
                final = rows*column
print(final)
