def isPrime(n) : 
  
    # Corner cases
    allprime = [True for i in range(ma+1)]

    p=2
    x = [0]*(n+1)
    while (p*p<=n):
        if allprime[p]==True:
        
            for i in range(p*p,n+1,p):
                allprime[i] = False
        p+=1
    for i in range(2,len(allprime)):
        if allprime[i]:
            x[i] = x[i-1]+1
        else:
            x[i] = x[i-1]
    return x
ma = 100005
x = isPrime(ma)
t = int(input())
for _ in range(t):
    m,n = list(map(int,input().split()))
    if m==1:
        m =2
    
    #print("ALl Prime lsit",allprime)
    no_of_prime = x[n]-x[m-1]
    print(no_of_prime*(n-m-no_of_prime+1))
