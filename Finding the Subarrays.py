n = int(input())
l1 = list(map(int,input().split()))
ma = pow(10,7)
ind1= [0]*(ma)
ind2 = [0]*(ma)
temp=0 

for i in range(n):
    r = sum(l1)
    l = 0
    for j in range(i,n):
        l+= l1[j]
        r = r - l1[j]
        if(n== j-i+1 or l/(j-i+1)>r/(n-j+i-1)):
            #print(r)
            ind1[temp] = i+1
            ind2[temp] = j+1
            #print(ind1[temp],ind2[temp])
            temp+=1
print(temp)
for i,j in zip(ind1,ind2):
    if i>0 or j>0:
        print(i,j)
