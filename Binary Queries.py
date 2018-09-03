n,q = map(int,input().split())
l =list(map(int,input().split()))
q2 = [[ None for _ in range(3)] for _ in range(q)] 
for i in range(q):
    
    q2[i] = list(map(int,input().split()))
    if q2[i][0] ==1:
        if l[q2[i][1]-1] ==0:
            l[q2[i][1]-1]=1
        else:
            l[q2[i][1]-1]=0
    else:
         
        if l[q2[i][2]-1]==0:
            print('EVEN')
        else:
            print('ODD')
