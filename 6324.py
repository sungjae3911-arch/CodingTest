import re
output = ["Protocol = ",'Host     = ','Port     = ','Path     = ']
for i in range(1, int(input())+1):
    s = input()
    p = re.match('(http|ftp|gopher)://([\\w.-]+)(?::([\\d]+))?(?:/([\\S]+))?',s)
    print(f"URL #{i}")
    for j, k in enumerate(output,1):
        print(f"{k}{p.group(j)}".replace("None","<default>"))
    print()