#!python3
n,k=list(map(int, input().split()))
a =list(map(int, input().split()))
b=0
c=a[k-1]  

for d in range(0,int(n)):
    if a[d] >= c and a[d] > 0:
        b+=1
print(b) 
