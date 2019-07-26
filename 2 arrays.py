n = int(input())
arr = list(map(int,input().split()))
brr = list(map(int,input().split()))
aneg = 0
bneg = 0
asum = 0
bsum = 0
for i in range(n):
    if arr[i]== -1:
        aneg +=1
    else:
        asum +=arr[i]
    if brr[i] == -1:
        bneg +=1
    else:
        bsum +=brr[i]
d = abs(asum - bsum)       
if aneg ==bneg:
    print("Infinite")

if (bsum-asum)>0 and aneg != bneg:
    if aneg == 0:
        print(0)
    if aneg==1:
        print(1)
    elif aneg>1:
        print(d+1)
        
if (asum-bsum)>0 and aneg!=bneg:
    if bneg == 0:
        print(0)
    if bneg==1:
        print(1)
    elif bneg>1:
        print(d+1)
        
