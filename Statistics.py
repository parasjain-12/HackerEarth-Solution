# Write your code here
n = int(input())
arr = []
for i in range(n):
    l = input().split()
    arr.append(l)
    
from collections import Counter,OrderedDict 

d = Counter(OrderedDict())
for i in range(len(arr)):
    x = str(arr[i][1])
    #print(x,type(x))
    if d[x]:
        d[x]+=1
    else:
        d[x]=1
    
    
temp = max(d.values())

for k,v in d.items():
    if v==temp:
        print(k)
        break
print(d['football'])
