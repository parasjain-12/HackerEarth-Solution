n = int(input())
l = list(map(int,input().split()))

ans = [1]
le = [1]
#d = {}
#d[1] =1
for i in range(1,n):
    
    if l[i]==1:
        if ans[i-1]+ 1 >=1:
            
            ans.append(ans[i-1]+1)
            #d[ans[i-1]+1] = i+1
            le.append(le[-1]+1)
            #print(i+1,d[ans[i-1]+1])
        else:
            #d[1] = 1
            le.append(1)
            ans.append(1)
    else:
        ans.append(ans[i-1]-1)
        le.append(le[-1]+1)
        
x= []
ma = max(ans)
for i in range(len(ans)):
    if ans[i]==ma:
        x.append(i)
final_ans= []
for i in range(len(x)):
    final_ans.append(le[x[i]])
    
print(max(final_ans))
