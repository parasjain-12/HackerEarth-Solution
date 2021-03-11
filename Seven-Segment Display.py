# Write your code here
d = {'0': 6,
     '1': 2,
     '2': 5,
     '3': 5,
     '4':4,
    '5':5,
    '6':6,
    '7':3,
    '8':7,
    '9':6}
t  = int(input())

for _ in range(t):
    n = input()
    no_of_matchstick = 0
    for i in n:
        no_of_matchstick += d[i]

    #Case 1 Max number when the no_of Matchstick is even
    if no_of_matchstick%2 == 0:
        x = int(no_of_matchstick/2)
        number = ''
        for i in range(x):
            number = number + '1'
    else:
        x = int((no_of_matchstick-3)/2)
        number = '7'
        for i in range(x):
            number = number + '1'

    print(number)
