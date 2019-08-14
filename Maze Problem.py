def issafe(p,q,arr):
    #print(type(p),type(n))
    if p<n and p>=0 and q<n and q>=0 and arr[p][q]==1:
        #print("Sdsdsd")
        return True
    return False
    
def solve(arr,i,j,sol):
    #print(n)
    if i==n-1 and j==n-1:
        sol[i][j]=1
        return True
    #print(i,j)
    if issafe(i,j,arr)==True:
        sol[i][j]=1
        #print(sol)
        
        if solve(arr,i,j+1,sol)==True:
            return True
        if solve(arr,i+1,j,sol)==True:
            return True
        sol[i][j]=0
        return False
        
        
t = int(input())
for _ in range(t):
    n = int(input())
    arr =[]
    sol = [[ 0 for i in range(n) ] for i in range(n)]

    for i in range(n):
        x = list(map(int,input().split()))
        arr.append(x)
        
    if solve(arr,0,0,sol) ==True:
        print("POSSIBLE")
    else:
        print("NOT POSSIBLE")
