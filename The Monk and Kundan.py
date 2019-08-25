def index(ref,x):
    for i in range(len(ref)):
        if ref[i]==x:
            return i
            
ref = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ref  = list(ref)
n = int(input())
for i in range(n):
    l = list(input().split())
    

    
    s=0
    for i in range(len(l)):
        for j in range(len(l[i])):
            t= index(ref,l[i][j])
            s+=j+ t
    print(s*len(l))
