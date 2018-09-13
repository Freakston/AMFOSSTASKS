#!python3
i=int(input())
while (i):
    word=str(input())
    l=len(word)
    if (l > 10):
         print(word[0] + str(len(word[1:-1])) + word[-1])
    else:
         print(word)
               
    i -= 1

