import sys
 
def index(t,f,ma,p,q,s,d):
    if f>ma:
        return 0 
    if t==0:
        for k,v in d.items():
            
            if v >= f:
                return k
    else:
        if f not in s:
            return 0
        else:
            return p[q.index(f)]
from collections import OrderedDict
 
n = sys.stdin.readline()
array = list(map(int, sys.stdin.readline().split()))
d = OrderedDict()
for i in array:
    #print(i)
    if i in d:
        d[i] +=1
    else:
        d[i] = 1
#print(d)
 
ma= max(d.values())
k = list(d.keys())
v = list(d.values())
s = set(v)
 
 
for i in range(int(sys.stdin.readline())):
    t,f = map(int, sys.stdin.readline().split())
    print(index(t,f,ma,k,v,s,d))
