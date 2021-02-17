test_cases = int(input())
for i in range(test_cases):
    p,g = map(int, input().split())
    n = int(input())

    cost = 0
    lower = min(p,g)
    maximum = max(p,g)
    p1_total = 0
    p2_total = 0
    for i in range(n):
        p1,p2 = map(int, input().split())
        p1_total += p1
        p2_total += p2

    if p1_total >= p2_total:
        cost += p1_total*lower
        cost += p2_total*maximum
    else:
        cost += p2_total*lower
        cost += p1_total*maximum
    print(cost)
