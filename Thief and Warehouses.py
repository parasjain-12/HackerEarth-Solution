def solve (array, n):
    stack = []
    i=0
    max_a=0
    area = 0
    while i<len(array):
        if  not stack or (array[stack[-1]]<=array[i]):
            stack.append(i)
            i+=1
            #print(stack)
        else:
            top = stack.pop()
            if stack:
                area = array[top]*(i-1-stack[-1])
            else:
                area =  array[top]*(i)
        max_a = max(max_a,area)
    while stack:
        top = stack.pop()
        if stack:
                area = array[top]*(i-1-stack[-1])
        else:
            area =  array[top]*(i)
            
        max_a = max(max_a,area)
    return max_a
    # Write your code here

T = int(input())
for _ in range(T):
    n = int(input())
    Ar = list(map(int, input().split()))

    out_ = solve(Ar, n)
    print (out_)
