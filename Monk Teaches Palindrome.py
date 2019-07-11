t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    if s == s[::-1]:
        if n%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")
