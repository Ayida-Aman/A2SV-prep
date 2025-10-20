# problem link: https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i, j = 0,0
result = []
while i<n or j<m:
    if i<n and (j==m or a[i] < b[j]) :
        result.append(a[i])
        i+=1
    else:
        result.append(b[j])
        j+=1

print(*result)