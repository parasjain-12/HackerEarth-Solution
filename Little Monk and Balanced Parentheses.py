n = int(input())
a = list(map(int,input().split()))
s = []
ans = 0
 
for i in range(0,n):
    if a[i] > 0:
        s.append(i)
    elif a[i] < 0:
        if s and a[i] == -a[s[-1]]:
            s.pop()
            if not s:
                temp = -1
            else:
                temp = s[-1]
            ans = max(ans,i - temp)
        else:
            s.append(i)
 
print(ans) 
