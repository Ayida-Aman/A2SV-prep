n, s = map(int, input().split())
a = list(map(int, input().split()))

l,total, res = 0,0,0,

for r in range (len(a)):
    total+=a[r]
    if total > s :
        total-=a[l]
        l+=1
    res= max(res, r-l+1)
print(res)