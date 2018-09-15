#!python3

sort=str((input()))
n=len(sort)
s=list()

for x in range(0,n):
    s.append(sort[x])

for y in range(0,n):
    for i in range(0,n-1):
        if (s[i] > s[i+1]):
                s[i],s[i+1] = s[i+1],s[i]
print(s)
