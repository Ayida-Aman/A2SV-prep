# problem link : https://codeforces.com/problemset/problem/1832/B
t = int(input())
for _ in range (t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    nums.sort()
    total = 0
    while k>0 and len(nums)>2:
        if nums[0] + nums[1] > nums[-1]:
            nums.pop(-1)
        else:
            nums.pop(0)
            nums.pop(0)
        k-=1
    total += sum(nums)
    print (total)