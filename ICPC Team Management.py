t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    
    from collections import Counter
    d = Counter()
    
    s = 0
    for i in range(n):
        temp = input()
        d[len(temp)] +=1
        
    c=0
    for x,v in d.items():
        #print(v)
        if v%k==0:
            c+=1
        

    if c==len(d):
        print("Possible")
        
    else:
        print("Not possible")
