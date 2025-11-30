nums = list(map(int, input().split()))
n = int(input())
i=0
while i < n:
    if nums[i] != nums[nums[i]]:
        nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
    else:
        i+=1

for i, num in enumerate(nums):
    if i != num:
        print(num)
        