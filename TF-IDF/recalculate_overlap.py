import os

store = "C:\\Users\\Night\\Documents\\Code\\Python\\store\\"

folders = os.listdir(store)

for folder in folders:
    folder_path = store + folder + "\\"
    files = os.listdir(folder_path)
    files.sort(key=lambda x: int(x[:-4]))
    output = open("C:\\Users\\Night\\Documents\\Code\\Python\\npm_projects\\diff\\" + folder + "_report.txt", 'w',
                  encoding='UTF-8')

    for file in files:
        now_file = folder_path + file
        #print(now_file)

        f = open(now_file)
        lines = f.readlines()
        f.close()

        file_index = file.split(".")[0]
        same_line = 0
        orphan_line_1 = 0
        orphan_line_2 = 0
        difference_line = 0
        for line in lines:
            #print(line)
            t = line.split(" ")[0]
            if "same line" in line:
                same_line = int(t)  # changed from same_line = int(line[0])
            elif "important left orphan line" in line:
                orphan_line_1 = int(t)
            elif "important right orphan line" in line:
                orphan_line_2 = int(t)
            elif "important difference line" in line:
                difference_line = int(t)
            elif "Left file: " in line:
                first_file = line.split(": ")[1]
            elif "Right file: " in line:
                second_file = line.split(": ")[1]

        output.write(file_index + "\n")
        output.write("first file: " + first_file)
        output.write("second file: " + second_file)
        output.write("same line: " + str(same_line) + "\n")
        output.write("orphan_line_1: " + str(orphan_line_1) + "\n")
        output.write("orphan_line_2: " + str(orphan_line_2) + "\n")
        output.write("difference_line: " + str(difference_line) + "\n")

        if same_line == 0:
            overlap = 0
            contained_1 = 0
            contained_2 = 0
        else:
            overlap = same_line / (same_line + orphan_line_1 + orphan_line_2 + difference_line)
            contained_1 = same_line / (same_line + orphan_line_1 + difference_line)
            contained_2 = same_line / (same_line + orphan_line_2 + difference_line)

        output.write("overlap: " + str(overlap) + "\n")
        output.write("contained of the first file: " + str(contained_1) + "\n")
        output.write("contained of the second file: " + str(contained_2) + "\n")
        output.flush()
    output.close()

