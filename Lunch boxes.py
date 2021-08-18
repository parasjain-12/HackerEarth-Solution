'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

t = int(input())
for _ in range(t):
    n,m =  map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    count = 0
    su = 0
    for i in range(len(a)):
        if a[i]+su <= n:
            su+=a[i]
            count+=1

    print(count)
