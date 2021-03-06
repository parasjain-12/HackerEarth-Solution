t = int(input())
for _ in range(t):
    sh,sm,eh,em = list(map(int,input().split()))
    starting_min = sh*60 + sm
    ending_min = eh*60 + em
    temp = ending_min  - starting_min
    if temp>=60:
        hr = int(temp/60)
        mi = temp - hr*60
    else:
        hr = 0
        mi = temp
    print(hr,mi)
