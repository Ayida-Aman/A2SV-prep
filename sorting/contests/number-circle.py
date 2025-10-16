# problem link : https://codeforces.com/gym/491686/problem/B

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

if arr[-2] + arr[-3] > arr[-1]:
    print("YES")
    arr[-2], arr[-1] = arr[-1], arr[-2]
    print(*arr)
else:
    print("NO")