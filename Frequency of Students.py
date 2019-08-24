# Write your code here
n = int(input())
d = {}
for _ in range(n):
    x = input()
    if x in d:
        d[x]+=1
    else:
        d[x]=1
for k,v in sorted(d.items()):
    print(k, v)
