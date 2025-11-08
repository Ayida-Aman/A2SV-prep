# problem link: https://codeforces.com/gym/491693/problem/A

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    count =0

    b = [a[0]]
    for i in range (1, len(a)):
        if a[i] != a[i-1]:
            b.append(a[i])
    for r in range (len(b)):
        left = b[r-1] if r>0 else float("inf")
        right = b[r+1] if r< len(b) -1 else float("inf")
        if b[r] < left and b[r] < right:
            count +=1
    print ("YES" if count ==1 else "NO")