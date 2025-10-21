# # problem link: https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/C
# from collections import Counter

# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# i, j = 0, 0
# count = 0
# while i<n and j<m:
#     if a[i]<b[j]:
#         i+=1
#     elif a[i] > b[j]:
#         j+=1
#     else:
#         num_i =a[i] 
#         count_a = 0
#         while i<n:
#             if a[i] == num_i:
#                 count_a+=1
#                 i+=1
        
#         num_j = b[j]
#         count_b = 0
#         while j<m:
#             if b[j] == num_j:
#                 count_b+=1
#                 j+=1
#         count += count_a*count_b
# print(count)        

from collections import Counter

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count_b = Counter(b)
total_pairs = 0

for num in a:
    total_pairs += count_b[num]

print(total_pairs)