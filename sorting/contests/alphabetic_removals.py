# problem link: https://codeforces.com/problemset/problem/999/C

from collections import Counter
n,k = map(int, input().split())
s = list(input())

remove_count = Counter()

for ch in sorted(set(s)):
    for i in range(len(s)):
        if ch == s[i] and k>0:
           remove_count[ch] +=1
           k-=1
        if k == 0:
            break;
    if k==0:
        break;
        
result = []

for ch in s:
    if remove_count[ch] > 0:
        remove_count[ch] -=1;
    else:
        result.append(ch)
        
print(''.join(result))