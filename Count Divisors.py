l,r,k = map(int,input().split())
c=0
for i in range(l,r+1):
    if i%k==0:
        #print(i)
        c+=1
print(c)
