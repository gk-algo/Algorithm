#https://www.acmicpc.net/problem/2295
n = int(input())
u = set()
for i in range(n):
    u.add(int(input()))
sums = set()
for i in u:
    for j in u:
        sums.add(i + j)
ans = {}
for i in u:
    for j in u:
        if (i - j) in sums:
            ans[i] = (i, j, i - j)
keys = list(ans.keys())
keys.sort()
print(keys[-1])