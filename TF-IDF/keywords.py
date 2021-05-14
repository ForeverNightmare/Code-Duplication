


f = open("keyword.txt")
output = open("js_keywords.txt", 'w')
lines = f.readlines()

for line in lines:
    k = line.split(" ")
    for keyword in k:
        output.write("\"" + keyword + "\"" + ", ")
    output.write("\n")
