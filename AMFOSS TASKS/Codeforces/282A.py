#!python3

n=int(input())
b=0
while n :
    a=input()
    if ('++X' or 'X++') in a:
     b+=1

    if ('--X' or 'X--') in a:
     b-=1

    n-=1
print(b)    
