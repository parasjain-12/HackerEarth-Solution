n = int(input())
l = [20,30,40,90,80]
if n>len(l):
    for i in range(5,n+1):
        if i%2==0:
            l.append(2*l[i-2])
        else:
            l.append(3*l[i-2])
y=0
for i in range(n):
    for j in range(i+1,n):
        ma = abs(l[i]+l[j])+abs(l[i]-l[j])
        y  = max(y,ma)
print(y)
