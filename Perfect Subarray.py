n = int(input())
l = list(map(int,input().split()))

import math
def checkperfect(n):
    i = int(math.sqrt(n))
    if n==i*i:
        return True
    else:
        return False


c=0
for i in range(n):
    s= 0
    for j in range(i,n):
        s+=l[j]
        if checkperfect(s):
            c+=1
print(c)
