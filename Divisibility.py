#If the last element contions zero then only we can divide the number formed by taking the last number by 10
# Therefore we only need to check that whether the last element of the last number is zero or not.

N = int(input())
arr = list(map(int,input().split()))
ele = arr[N-1]
if ele % 10 == 0:
    print("Yes")
else:
    print("No")
