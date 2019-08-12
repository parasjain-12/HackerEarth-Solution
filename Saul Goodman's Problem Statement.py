from collections import defaultdict 

t = int(input())
for _ in range(t):
    n = int(input())
    ans=0
    d1=defaultdict(int)
    d2=defaultdict(int)
    for i in range(n):
    
        a,b=map(int,input().split())
        ans+=d1[a+b]
        ans+=d2[a-b]
        #print("sdsd",ans)
        
        
        d1[a+b]+=1 
        d2[a-b]+=1 
        #print(d1,d2)
    print(ans)
