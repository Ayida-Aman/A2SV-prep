n, s = map(int, input().split())
a = list(map(int, input().split()))

l, total = 0,0
res = float('inf')

for r in range(len(a)):
    total+=a[r]
    while total >= s:
        res = min(res, r-l+1)
        total-=a[l]
        l+=1
        
print (res if res != float('inf') else 0)


n, s = map(int, input().split())
a = list(map(int, input().split()))

l, total = 0,0
res = float('inf')

for r in range(len(a)):
    total+=a[r]
    while total - a[l] > s:
        total-=a[l]
        l+=1
    if total>=s:
        res = min(res, r-l+1)
print (res if res != float('inf') else 0)
