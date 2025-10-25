# problem link: https://codeforces.com/problemset/problem/1073/E

n, s = map(int, input().split())
a= list(map(int, input().split()))

l, res, total = 0,0,0

for r in range (n):
    total +=a[r]
    while total > s:
        total -=a[l]
        l+=1
    res += r-l+1
print (res)