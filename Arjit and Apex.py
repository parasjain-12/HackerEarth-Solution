t = int(input())
for _ in range(t):
    m,n = map(int,input().split())
    d = dict()
    new = dict()
    for i in range(m):
        p,q = map(int,input().split())
        d[i] = (p,q)
    for i in range(n):
        p,q = map(int,input().split())
        new[i] = (p,q)
    g,h = map(int,input().split())
    g_c = 0
    h_c=0
    
    i = 0
    j = 0
    while i<len(d):
        while j<len(new):
            if new[j][0]==d[i][0]:
                g_c+=1
                if new[j][1]==d[i][1]:
                    h_c+=1
                
                i+=1
            j+=1
        break
    #print(h_c,g_c)
    if h_c == h:
        print("Great")
    elif g_c == g:
        print("Good")
    else:
        print(":(")
