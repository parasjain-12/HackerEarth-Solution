
for _ in range(int(input())):
    n,a,b,c = map(int,input().split())
    
    #store the beetles with 0 or 1 
    #0 means start time 
    # 1 means end time 
    beetles  = []
    
    for i in range(n):
        x,y = map(int,input().split())
        beetles.append((x,0))
        beetles.append((y,1))
        
    # sort the array with my giving start time pripority and taking the consideration that endtime is less than the 
    #previous once
    beetles.sort(key = lambda b: b[0]*2+ b[1])
    
    total = n*a
    # since we have added a in starting , now we are adding b and substracting a
    ba = b-a
    cb = c-b
    max_ = total
    #checking whether the its the start time or end time 
    # If it is start time we are adding ba
    #if end time we are adding cb
    for b in beetles:
        if b[1]==0:
            total += ba
        else:
            total += cb
        max_ = max(max_,total)
    print(max_)
