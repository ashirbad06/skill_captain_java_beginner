file = open("data.txt", "r")
content = file.read()
lines = 1
if '\n' in content:
    lines = content.count('\n') + 1
file.close()
print(lines)
