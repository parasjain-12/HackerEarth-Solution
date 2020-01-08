while True:
    try:
        n = int(input())
        s = bin(n)
        print(s.count('1'))
    except:
        break
