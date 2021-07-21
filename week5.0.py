fname = open('fileTh.txt', 'r' ,encoding='utf8')
line_count = 0
char_count = 0

for line in fname:
    line_count += 1
    char_count += len(line)
print(line_count,"lines", char_count,"chars")

fname.close()
