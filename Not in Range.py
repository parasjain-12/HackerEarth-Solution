k = sum([i for i in range(1,1000001)])
t = int(input())
l = []
for _ in range(t):
    x,y = map(int,input().split())
    l.append([x,y])
    
l = sorted(l)
for i in range(len(l)-1):
    #print(i)
    if(l[i+1][0]<=l[i][1]):
        l[i+1][0] = l[i][1]+1

for i in range(len(l)):
    if(l[i][0]>l[i][1]):
        l[i] = 0
for i in range(len(l)):
    if(l[i]!=0):
        e = (l[i][1]*(l[i][1]+1))//2
        o = (l[i][0]*(l[i][0]+1))//2
        p = e-o+l[i][0]
        k-=p
print(k)
