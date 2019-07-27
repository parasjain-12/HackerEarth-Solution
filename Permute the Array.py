t = int(input())
from collections import Counter
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    count = int(n/k)
    a= Counter(arr)
    l2 = 0
    for p12,v in a.items():
        if v==count:
            l2+=1
            #print(l1)
        elif v>count:
            temp = int((v/count))
            l2+=temp
            #print(temp)
    if l2 ==k:
        print("YES")
    else:
        print("NO")
