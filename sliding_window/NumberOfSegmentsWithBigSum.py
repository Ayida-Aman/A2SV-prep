# problem link: https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/D
n, s = map(int, input().split())
a = list(map(int, input().split()))

l,total, res= 0,0,0

for r in range (n):
    total +=a[r]
    while total >= s:
        res += n-r
        total-=a[l]
        l+=1
print (res )