n = int(input())
a = list(map(int,input().split()))

tmp_sum = sum(a)
lucky = []
if n == 1:
    lucky.append(1)
else:
    for i in range(n):
        if i == 0:
            lucky.append(0)
        else:
            lucky.append(lucky[i-1])
        #print(lucky)
        if (tmp_sum - a[i])%3 == 0:
            if i == 0:
                if a[n-1] == 0:
                    lucky[i]+=1
            elif i == n-1:
                if a[n-2] == 0:
                    lucky[i]+=1
            else:
                if (a[i-1]+a[n-1])%10 == 0:
                    lucky[i]+=1
lucky.insert(0,0)   
q = int(input())
for _ in range(q):
    l,r = map(int,input().split())
    print(lucky[r] - lucky[l-1])
