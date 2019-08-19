n = int(input())
l = list(map(int,input().split()))
m = int(input())
i=0
temp = []
while i!=m:
    qq=[int(x) for x in input().split()]
    temp.extend(qq)

    if len(temp)>=2:
        p= temp.pop(0)
        q = temp.pop(0)

    
    
        new_array = l[p-1:q]
        print(len(set(new_array)))
        i+=1

    else:
        pass
