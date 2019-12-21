from fractions import Fraction
t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    c=0
    for j in range(4,n-4):
        #print(s[i])
        if (s[j] != 'a') and  (s[j] != 'e') and (s[j]!= 'i') and (s[j] != 'o') and (s[j] !='u') :
            c+=1

    print(c+4,end ='')
    print('/',end = '')
    print(n)
