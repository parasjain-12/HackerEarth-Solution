n = int(input())
for _ in range(n):
    s = input()
    from collections import Counter
    s2 = 'abcdefghijklmnopqrstuwvxyz'
    
    d = Counter(s2) 
    for i in range(len(s)):
        if s[i] in s2:
            if d[s[i]]:
                d[s[i]]+=1
            else:
                d[s[i]]=1
                #print(d[s[i]])
        else:
            d[s[i]]=0
            
    ans = sorted(d.items(), key = lambda x : (x[1],-ord(x[0])))
    for i in range(len(ans)):
        print(ans[i][0],end = ' ')
    print('\n')
