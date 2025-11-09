# problem link: https://codeforces.com/gym/491693/problem/D

n = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(nums)
l=0
res = 0
for r in range(len(nums)):
    while sorted_nums[r] - sorted_nums[l] > 5:
        l+=1
    res = max(res, r-l+1)
print(res)

# 1 2 10 12 15 17
