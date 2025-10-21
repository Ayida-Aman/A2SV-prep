# problem link: https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i, j= 0,0
counter = 0
result = []

while j<m:
    while i<n and a[i]<b[j]:
        counter+=1
        i+=1
    result.append(counter)
    j+=1
print(*result)