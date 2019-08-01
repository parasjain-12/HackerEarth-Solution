

# Write your code here
# To understand the question go to link : https://www.geeksforgeeks.org/largest-rectangle-under-histogram/
t = int(input())
for _ in range(t):
    n= int(input())
    ar = list(map(int,input().split()))
    flist = [0]*n
    stack = list()
    i=0
    while i<n:
        if not stack or ar[stack[-1]]>=ar[i]:
            stack.append(i)
            #print(stack)
            i+=1
        else:
            top = stack.pop()
            if not stack:
                flist[top] = top
                #print("flidggfd",flist[top])
            else:
                #print("top",top)
                flist[top] = top-stack[-1]
                #print("flist",flist[i])
    while stack:
        top = stack.pop()
        if not stack:
            flist[top] = top
            #print("sdfdf",flist[top])
        else:
                #print("top",top)
                flist[top] = top-stack[-1]
                #print("flist",flist[i])
    blist = [0]*n
    br = ar[::-1]
    #print(br)
    stack1 = list()
    i=0
    while i<n:
        if not stack1 or br[stack1[-1]]>=br[i]:
            stack1.append(i)
            #print(stack1)
            i+=1
        else:
            top = stack1.pop()
            if not stack1:
                blist[top] = top
                #print("flidggfd",blist[top])
            else:
                #print("top",top)
                blist[top] = top-stack1[-1]
                #print("flist",flist[i])
    while stack1:
        top = stack1.pop()
        if not stack1:
            blist[top] = top
            #print("sdfdf",blist[top])
        else:
                #print("top",top)
                blist[top] = top-stack1[-1]
                #print("flist",flist[i])
    backlist = blist[::-1]
    res_list = [] 
    for i in range(0, len(backlist)): 
        res_list.append(backlist[i] + flist[i])
    sight  = []
    for i in range(1,len(res_list)+1):
        sight.append((i*res_list[i-1])%1000000007)
    temp = sight.index(max(sight))+1
    print(temp)
