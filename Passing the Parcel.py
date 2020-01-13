'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n  = int(input())
st = [True]*n
song = input()
ne = len(song)
c = 0
j=0
i=0
while c<n-1:
    #print(i)
    if i>=ne:
        i = i%ne
    if j>=n:
        j = j%n
    if song[i] =='a':
        if st[j] != False:
            i+=1
            #st[j] == True
            j+=1
        else:
            j+=1
    elif song[i] == 'b':
        #print("sdsds")
        if st[j] != False:
            c+=1
            i+=1
            st[j] = False
            j+=1
        else:
            j+=1

for i in range(len(st)):
    if st[i] == True:
        print(i+1)
        break
