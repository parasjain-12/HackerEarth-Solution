l = list(input())
from collections import Counter
d = Counter(l)
temp = max(d.values())
li = []
for k,v in d.items():
    if v==temp:
        li.append(k)
        
li.sort(key= lambda x: ord(x))
print(li[0],d[li[0]])
