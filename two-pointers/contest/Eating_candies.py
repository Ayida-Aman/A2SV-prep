t = int(input())
for _ in range (t):
    n = int(input())
    nums = list(map(int, input().split()))

    i , j = 0, len(nums) -1
    half = sum(nums)//2
    totalAli, totalBob, counter = 0, 0, 0

    while totalAli + nums[i] < half and totalBob + nums[j] < half and i< j:
        totalAli+=nums[i]
        i+=1
        totalBob+=nums[j]
        j-=1    