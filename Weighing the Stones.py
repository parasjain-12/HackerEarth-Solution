from collections import Counter
testCase = int(input())
for _ in range(testCase):
    n = int(input())
    rupam = list(map(int,input().split()))
    ankit =  list(map(int,input().split()))
    r =Counter(rupam)
    a = Counter(ankit)
    mr_k= 0
    mr_v=0
    for k,v in r.items():
        #print(k,v)
        if v>=mr_v:
            if v>mr_v:
                mr_v = v
                mr_k = k
            else:
                if k>mr_k:
                    mr_k = k
                    mr_v = v
                
                
                
    mr = max(r.keys())
    if r[mr]>=mr_v:
        mr_k = mr

        
    ma_k= 0
    ma_v=0
    for k,v in a.items():
        #print(k,v)
        if v>=ma_v:
            if v>ma_v:
                ma_v = v
                ma_k = k
            elif v==ma_v:
                if k>ma_k:
                    ma_k = k
                    ma_v = v
            
            
    #print(ma_k)
    ma = max(a.keys())
    if a[ma]>=ma_v:
        ma_k = ma   
    
            
    if mr_k>ma_k:
        print('Rupam')
    elif mr_k<ma_k:
        print('Ankit')
    else:
        print("Tie")
