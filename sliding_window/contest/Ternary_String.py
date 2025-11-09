# problem link: https://codeforces.com/gym/491693/problem/C

t = int(input())

for _ in range(t):
    line = input().strip()
    arr = [int(ch) for ch in line]
    window = {}
    l=0
    res = float("inf")
    for r, num in enumerate(arr):
        window[num] = window.get(num, 0) +1

        while len(window) == 3:
            res = min(res, r-l+1)
            window[arr[l]] -=1
            if window[arr[l]] == 0:
                del window[arr[l]]
            l+=1

    print(res if res != float("inf") else "0")