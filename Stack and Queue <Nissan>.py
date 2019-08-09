n , k = map(int,input().split())
l = list(map(int,input().split()))

s = 0
for i in range(k):
    s += l[i]
    
m = s
#print(m)
for i in range(k-1):
    #print("sds",i)
    s = s - l[k-i-1] + l[n-1-i]
    if s>=m:
        m=s
print(m)
