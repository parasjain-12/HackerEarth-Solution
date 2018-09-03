s=int(input())
for i in range(s):
    n,r = map(int,input().split())
    l = list(map(int,input().split()))
    
    c=0
    ma = 0.5
    for i in range(len(l)):
        if l[i]>ma:
            ma = l[i]
            c+=1
    print(c*r)
