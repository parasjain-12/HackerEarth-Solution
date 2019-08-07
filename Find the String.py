t = int(input())
from collections import Counter
for _ in range(t):
    n,m = map(int,input().split())
    matrix = {}
    for i in range(n):
        a = list(input())
        matrix[i] = Counter(a)
    s = input()
    l = len(s)
    c = 0
    c = 0
    for i in range(len(s)):
        #print("fdefd",s[i],i)
        if i<n:
            if s[i] in matrix[i] and matrix[i][s[i]]>0:
                matrix[i][s[i]] -=1
                #print(matrix[i],s[i])
                c+=1
        else:
            j = i%n
            if s[i] in matrix[j] and matrix[j][s[i]]>0:
                matrix[j][s[i]] -=1
                #print("Else",matrix[j])
                c+=1
    if c==l:
        print("Yes")
    else:
        print("No")
