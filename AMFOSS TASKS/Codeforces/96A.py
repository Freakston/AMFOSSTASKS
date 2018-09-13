#!python3

n=input()

a=0

s=int(len(n))

for i in range(0,(s-1)):
    if n[i] == n[i+1]:
        a+=1
if a >= 7:
    print('Yes')
else:
    print('No')
    
