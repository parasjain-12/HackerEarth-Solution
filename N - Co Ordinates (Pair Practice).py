from collections import Counter
n = int(input())
d = Counter()
for i in range(n):
    x = tuple(map(int,input().split()))
    d[x]+=1

 
        
for k,v in sorted(d.items()):
    print(*k,v)
