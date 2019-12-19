def binar(arr,l,r,x):
    if r >=l:
        mid = int(l+ (r-l)/2)
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binar(arr,l,mid-1,x)
        else:
            return binar(arr,mid+1,r,x)
    else:
        return -1

n,m = map(int,input().split())
array = []
for i in range(n):
    temp = list(map(int,input().split()))
    array.append(temp)
    
q  = int(input())
for _ in range(q):
    x = int(input())
    f =0
    for i in range(n):
        t = binar(array[i],0,len(array[i])-1,x)
        if t!= -1:
            f=1
            break
    if f==1:
        print(i,t)
    else:
        print("-1 -1")
                
