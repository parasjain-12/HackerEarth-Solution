testCase  = int(input())
for _ in range(testCase):
    n = int(input())
    l = list(map(int,input().split()))
    c=1
    ma = l[0]
    
    for i in range(1,n):
        if l[i]<=ma:
            #print(l[i])
            c+=1
            ma = l[i]
    print(c)
