n,m = map(int,input().split())
arr = list(map(int,input().split()))

d = dict()
c= 0
for i in range(n):
    temp = m-arr[i]
    if d.get(temp):

        #print(arr[i],temp)
        c+= d[temp]
    if d.get(arr[i]):
        d[arr[i]] +=1
    else:
        d[arr[i]] =1   
print(c)
