for _ in range(int(input())):
    n, m = map(int, input().split())
    M = [list(map(int, input().split())) for __ in range(n)]
    
    for k in range(int(input())):
        t, x, y = map(int,input().split())
        s = 0
        if t == 1:
            if y % 2 == 0:
                if x-1 >= 0:
                    s += M[x-1][y]
                if x+1 < n:
                    s += M[x+1][y]
                if y-1 >= 0:
                    s += M[x][y-1]
                if y+1 < m:
                    s += M[x][y+1]
                if x-1 >= 0 and y-1 >= 0:
                    s += M[x-1][y-1]
                if x-1 >= 0 and y+1 < m:
                    s += M[x-1][y+1]
                print(s)
            else:
                if x-1 >= 0:
                    s += M[x-1][y]
                if y-1 >= 0:
                    s += M[x][y-1]
                if y+1 < m:
                    s += M[x][y+1]
                if x+1 < n and y-1 >= 0:
                    s += M[x+1][y-1]
                if x+1 < n:
                    s += M[x+1][y]
                if x+1 < n and y+1 < m:
                    s += M[x+1][y+1]
                print(s)
        else:
            if y % 2 == 0:
                if x-2 >= 0 and y-1 >= 0:
                    s += M[x-2][y-1]
                if x-2 >= 0:
                    s += M[x-2][y]
                if x-2 >= 0 and y+1 < m:
                    s += M[x-2][y+1]
                if x-1 >= 0 and y-2 >= 0:
                    s += M[x-1][y-2]
                if y-2 >= 0:
                    s += M[x][y-2]
                if x+1 < n and y-2 >= 0:
                    s += M[x+1][y-2]
                if x+1 < n and y-1 >= 0:
                    s += M[x+1][y-1]
                if x+2 < n:
                    s += M[x+2][y]
                if x+1 < n and y+1 < m:
                    s += M[x+1][y+1]
                if y+2 < m:
                    s += M[x][y+2]
                if x+1 < n and y+2 < m:
                    s += M[x+1][y+2]
                if x-1 >= 0 and y+2 < m:
                    s += M[x-1][y+2]
                print(s)
            else:
                if x-1 >= 0 and y-1 >= 0:
                    s += M[x-1][y-1]
                if x-2 >= 0:
                    s += M[x-2][y]
                if x-1 >= 0 and y+1 < m:
                    s += M[x-1][y+1]
                if x-1 >= 0 and y-2 >= 0:
                    s += M[x-1][y-2]
                if y-2 >= 0:
                    s += M[x][y-2]
                if x+1 < n and y-2 >= 0:
                    s += M[x+1][y-2]
                if x+2 < n and y-1 >= 0:
                    s += M[x+2][y-1]
                if x+2 < n:
                    s += M[x+2][y]
                if x+2 < n and y+1 < m:
                    s += M[x+2][y+1]
                if x+1 < n and y+2 < m:
                    s += M[x+1][y+2]
                if y+2 < m:
                    s += M[x][y+2]
                if x-1 >= 0 and y+2 < m:
                    s += M[x-1][y+2]
                print(s)
