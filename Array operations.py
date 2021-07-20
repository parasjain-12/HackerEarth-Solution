# Knowledge of Kadane algorithm 
#To understand the below algorithm I highly recommend you to visit https://www.geeksforgeeks.org/maximum-subarray-sum-possible-after-removing-at-most-one-subarray/ 


def kadaneSum(arr,n):
    new_arr = [0]*n
    curr_sum = s = 0
    for i in range(n):
        if curr_sum<0:
            curr_sum = 0
        if curr_sum + arr[i] >s:
            s = curr_sum + arr[i]
        curr_sum = curr_sum + arr[i]
        new_arr[i] = s
    return new_arr

t = int(input())
for _ in range(t):
    n = int(input())
    li = list(map(int,input().split()))
    pre_sum = kadaneSum(li,n)
    post_sum = kadaneSum(li[::-1],n)
    post_sum = post_sum[::-1]
    ans = 0
    for i in range(n-1):
        ans = max(ans,pre_sum[i]+post_sum[i+1])

    print(ans)
