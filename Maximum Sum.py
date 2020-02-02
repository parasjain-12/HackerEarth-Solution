n = int(input())
arr=  list(map(int,input().split()))
s = 0
c = 0
for i in range(len(arr)):
    if arr[i]>=0:
        s += arr[i]
        c +=1
        
if s==0 and c==0:
    s = max(arr)
    c = 1
print(s,c)
