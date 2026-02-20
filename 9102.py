import sys

n = int(input())

for _ in range(n):
    vps = input()
    stack = []
    for t in vps:
        if t == '(':
            stack.append(t)
        elif t == ')':
            if not stack:
                print("NO")
                break
            else:
                stack.pop()
    else:
        if not  stack:
            print("YES")
        else:
            print("NO")


