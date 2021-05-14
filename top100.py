f = open("top100.txt")

output = open("top-100.txt", 'w')

lines = f.readlines()

for line in lines:
    k = line.split(" ")
    if not k[0].startswith("@"):
        output.write(k[0])
        output.write("\n")
