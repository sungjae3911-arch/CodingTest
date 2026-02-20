import sys
n, m = map(int, input().split())

arrayS = set()

for i in range(n):
    s = sys.stdin.readline()
    arrayS.add(s)

cnt = 0
for _ in range(m):
    t = sys.stdin.readline()
    if t in arrayS:
        cnt += 1

print(cnt)