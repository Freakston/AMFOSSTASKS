#!python3

string =input()
i = 1
c = 0
b = 3
while (i <= 3):
    if list(string[c:b]) == list(reversed(string[c:b])):
        print('Palindrome')
    else:
        print('Not a palindrome')
    c+=3
    b+=3
    i+=1

 
    

          

