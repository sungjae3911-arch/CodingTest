a = input().split()

strType = a.pop(0)
for i in a:
    res = strType
    for j in range(len(i)-2, -1, -1):
        if i[j] == "*" or i[j] == "&":
            res += i[j]
        elif i[j] == "]":
            res += "[]"
        elif i[j] == "[":
            continue
        else :
            name = i[:j+1]
            break
    print(res, name + ";")