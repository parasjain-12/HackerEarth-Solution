n = int(input())
l = []
for _ in range(n):
    a = tuple(map(int,input().split()))
    a = sorted(a)
    
    l.append(tuple(a))

from collections import Counter

d = Counter(l)
ans = 0
for k,v in d.items():
    if v ==1 :
        ans+=1
        
print(ans)
