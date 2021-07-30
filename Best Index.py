
## Explaination : 
'''
Step 1 : First we will find out till what index the zeroth index can go for example consider the array [1,3,1,2,5] here the zeroth index can go till index 2 and
k = 2 k = partition that is 1,2,3. This k will tell us the much indeed information to solve the question this tells us that how many elements are picked .So 
If for index zeroth the k value is 2 we can't have k >2 for any other index.(TRY with example ). 

The above step is done from line 20 to 30.

Step 2: Now we will start a loop from index 1 as we have already cover the case for index 0. 
      2.a : We will first substract the previous value as we have added that in the step 1 and we don't need that now(because we have increase the index).
      2.b : Then we will check whether the index 0 has reach the end or not: if index 0 has reach the end then the next index won't have same k value. 
          Therefore we will decrese the k and subtract those value from the initialSum.
          
          If the index 0 has not reach the end :: Only one element is added.(Try to analyze with example )
'''

# Write your code here
n = int(input())
a = list(map(int,input().split()))
start = 1
k = 2
while start<=n:
    start += k
    k+=1

start -= k-1
k-=2
initialSum = sum(a[:start])
ma = initialSum

for i in range(1,n):
    initialSum -= a[i-1]
    if start<n:
        initialSum += a[start]
        start+=1
    else:
        k-=1
        initialSum -= sum(a[n-k:n])
        start -= k
    if initialSum > ma:
        ma =initialSum
print(ma)
