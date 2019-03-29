
def prime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return 0
    if (n <= 3) : 
        return 1
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return 0
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return 0
        i = i + 6
  
    return 1

t = int(input())
for _ in range(t):
    n = int(input())
    x = prime(n)
    if n==2:
        print('NO')
    elif n==1:
        print('YES')
    elif x==1:
        print('YES')
    elif x==0:
        y = prime(n+1)
        
        
        if y==1:
            print('NO')
        else:
            print('YES')
