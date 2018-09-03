# Write your code here
def prime(x):
    l = [True for i in range(x+1)]
    p=2
    while (p*p <= x):
        if l[p]==True:
            for i in range(2*p,x+1,p):
                l[i] = False
        p+=1
    for i in range(2,x+1):
        if l[i]:
            print(i,end=' ')
            
n  = int(input())
prime(n)
