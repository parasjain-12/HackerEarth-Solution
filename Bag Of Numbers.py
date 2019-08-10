n=input().split()
if (len(n)<4):
    n[0]="output"
else:
    n[0]="output:"
print(*n)
