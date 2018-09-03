from collections import Counter
n =int(input())
l = Counter(list(map(int,input().split())))
x = 100000
for k,v in l.items():
    if v==max(l.values()):
        x = min(x,k)
print(x)
