t = int(input())
for i in range(t):
    n,p,q,r = map(int,input().split())
    c=0
    for i in range(1,n+1):
        if (i%p==0)and (i%q!=0)and (i%r!=0):
            c+=1
        if (i%p!=0)and (i%q==0)and (i%r!=0):
            c+=1
        if (i%p!=0)and (i%q!=0)and (i%r==0):
            c+=1
    print(c)
