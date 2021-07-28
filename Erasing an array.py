#When we encounter 1,0 sequence we have inversion and we can't erase the solution 
#Therefore the simple solution here is to just count the number of inversion that is the sequence of 1 follwed by 0.


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    c = 1
    for i in range(n-1):
        if arr[i] == 1 and arr[i+1]==0:
            c+=1
    print(c)
