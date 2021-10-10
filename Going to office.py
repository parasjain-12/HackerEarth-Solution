'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
d = int(input())
oc,of,od = map(int,input().split())
cs,cb,cm,cd = map(int,input().split())
temp = d- of
if temp > 0:
    costOnline = oc+ temp*od
else:
    costOnline = oc

time = d//cs
costOffline = cb + cm*time + cd*d

if costOnline<=costOffline:
    print("Online Taxi")

else:
    print("Classic Taxi")
