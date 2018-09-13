#!python3
a=input()
b=input()

for i in range(len(a)):
    c=a[i].upper()
    d=b[i].upper()

    if ord(c)>ord(d):
        print('+1')
        exit()

    elif ord(c)<ord(d):
       print('-1')
       exit()  
    else:
        continue
print('0')
