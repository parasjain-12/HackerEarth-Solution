n = int(input())
s = input()
a = 0
e=0
i=0
o=0
u=0
for j in range(n):
    if s[j]=='a':
        a+=1
    if s[j]=='e':
        e+=1
    if s[j]=='i':
        i+=1
    if s[j]=='o':
        o+=1
    if s[j]=='u':
        u+=1
        
if a>0 and e>0 and i>0 and o>0 and u>0:
    print("YES")
else:
    print("NO")
        
