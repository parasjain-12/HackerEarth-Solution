n = int(input())
l = input()

s1 = l.count('1')
s2 = l.count('0')
s= l.split('0')

m  = 0
for i in range(len(s)-1):
    z=s[i].count("1")+s[i+1].count("1")
    if(z>m):
        m=z
if(s2==0):
    print(s1)
elif(s1==0):
    print(0)
elif(s1>m):
    print(m+1)
else:
    print(m)
