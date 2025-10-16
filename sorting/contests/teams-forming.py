# problem link : https://codeforces.com/gym/491686/problem/A

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
total = 0

for i in range(len(arr) - 1):
    total += arr[i + 1] - arr[i]

print(total)
