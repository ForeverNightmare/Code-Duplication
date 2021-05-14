import os



file_level_path = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_file_level_0.5\\"

files = os.listdir(file_level_path)
output = open(file_level_path + "analysis.csv", "w")
for file in files:
    if file.endswith("file_level.txt"):
        text = open(file_level_path + file)
        lines = text.readlines()
        if len(lines) >= 3:
            for line in lines:
                t = line.split(" ")
                if len(t) == 2 and t[1] != "0\n":
                    output.write(t[0] + ",")
                    if "config" in t[0] or "index" in t[0] or "conf." in t[0] or "example" in t[0]:
                        output.write("0" + "\n")
                    elif "test." in t[0] or "test@" in t[0] or "@test" in t[0]:
                        output.write("2" + "\n")
                    else:
                        output.write("1" + "\n")
        output.write("," + "\n")




