# Simple Brute force implementation
# Only thing to note here is that in the dictonary/HaspMap we are storing key and list of values 


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    d= {}

    for i in range(len(a)):
        try:
            if d[a[i]]:
                d[a[i]].append(i+1)
        except:
            d[a[i]] = [i+1]


    ans = 0
    for k,v in d.items():
        if len(v)>=2:
            ans += v[-1] - v[0]

    print(ans)
