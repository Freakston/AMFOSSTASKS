#!python3
n=int(input())
k=list(map(int, input().split()))

a=0
b=0
c=0
d=0

while n:
    if (k[0] == 1) and (k[1] == 1) and (k[2] == 1):
        a+=1    
    elif (k[0] == 1) and (k[2] == 1):
        b+=1
    elif (k[0] == 1) and (k[1] == 1):
        c+=1
    elif (k[1] == 1) and (k[2] == 1):
        d+=1
print(a+b+c+d)
        
