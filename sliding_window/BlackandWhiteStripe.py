# problem link: https://codeforces.com/problemset/problem/1690/D

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = list(input())
    Wcount = s[:k].count("W")
    min_W = Wcount

    for i in range(k, n):
        if s[i-k] == "W":
            Wcount -=1
        if s[i] =="W":
            Wcount+=1
        min_W = min(min_W, Wcount)
    print(min_W)