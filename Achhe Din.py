testCase = int(input())
from collections import Counter
for _ in range(testCase):
    n = int(input())
    ide = Counter(list(map(int,input().split())))
    print(list(ide.keys())[list(ide.values()).index(1)])
