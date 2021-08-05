#Logic : Since there are n students and each student will recienve atleast one chocalate and the next student will receive k+1(Assuming k is the no.of chocolate given to first student)
# then next student will get k+2,k+3.... so on
# Minimum no.of chocolate n student will get will be n*(n+1)//2 where n = no.of student
#Step 2: Calculate the chocalte left that is : c - ( Minimum no.of chocolate)
# Step3 : Ans = chocalte left % n
#Let us understand via example : c = 20 n = 3
# Since there are 3 student they are bound to recieve 6 chocolate 
#chocolateLeft = 20 -6 = 14
# If we divide 14 //3 we get 4 
# therefore we can give each student 4 more chocolate that 5,6,7 = 18
#Therefore ans  = 20 - 18
#Below is a shortcut way to calculate the above



t = int(input())
for _ in range(t):
    c,n = map(int,input().split())
    minimumChocolates = (n*(n+1))//2
    if minimumChocolates >= c:
        print(c)
    else:
        c = c - minimumChocolates
        ans = c%n
        print(ans)
