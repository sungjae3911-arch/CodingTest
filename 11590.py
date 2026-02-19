n = int(input())

h = list(map(int, input().split()))
balloonList = [0] * (n + 1)

result = 0
for i in h:
    if balloonList[i] == 0:
        balloonList[i-1] += 1
    else:
        balloonList[i] -= 1
        balloonList[i - 1] += 1

print(sum(balloonList))