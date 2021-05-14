import os
import subprocess
import time

basic = r"BCompare.exe /silent "
script = r"@C:\Users\Night\Documents\Code\Python\npm\scrpit_summary.txt "

class_path = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_1130_class\\"
#file_output = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_projects\\report.txt"
big_parameter = 5
store = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_report\\"
folders = os.listdir(class_path)

folders.sort(key=lambda x: int(x))

bug = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_report\\bugs.txt"
bug_output = open(bug, 'w', encoding='UTF-8')
cmd_file = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_report\\cmd.txt"
cmd_output = open(cmd_file, 'w', encoding='UTF-8')

start = time.time()
for folder in folders:
    print(folder)
    now = -1
    if not os.path.exists(store + folder):
        os.makedirs(store + folder)
    folder_path = class_path + folder + "\\"
    files = os.listdir(folder_path)
    numbers = len(files)
    js_files = []
    for i in range(numbers):
        if files[i].endswith(".js"):
            js_files.append(files[i])
    output = open("C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_diff\\" + folder + "_report.txt", 'w',
                  encoding='UTF-8')
    js_numbers = len(js_files)
    for i in range(js_numbers):
        for j in range(i+1, js_numbers):
            file_1 = js_files[i]
            file_2 = js_files[j]
            #print(file_1 + ' ' + file_2)
            prefix_1 = file_1.split("@")[0]
            prefix_2 = file_2.split("@")[0]
            file_1_path = folder_path + file_1
            file_2_path = folder_path + file_2
            file_1_size = os.path.getsize(file_1_path)
            file_2_size = os.path.getsize(file_2_path)
            bigger = max(file_1_size, file_2_size)
            smaller = min(file_1_size, file_2_size)
            #print(bigger)
            #print(smaller)
            #print(prefix_1 != prefix_2)
            #print(smaller*10 >= bigger)
            if prefix_1 != prefix_2 and smaller * big_parameter >= bigger and smaller != 0:
            #if prefix_1 != prefix_2 and smaller != 0 and bigger != 0:
                #print(file_1_path + ' ' + file_2_path)
                now += 1
                file_output = store + folder + "\\" + str(now) + ".txt"
                #file_output = r"C:\Users\Night\Documents\Code\Python\npm\report1.txt"
                cmd = basic + script + file_1_path + ' ' + file_2_path + ' ' + file_output
                cmd_output.write(str(folder) + ' ' + str(now) + ' ' + file_1_path + ' ' + file_2_path + "\n")
                cmd_output.flush()
                os.system(cmd)
                if not os.path.exists(file_output):
                    bug_output.write(file_1_path + ' ' + file_2_path + "\n")
                    bug_output.flush()
                else:
                    f = open(file_output)
                    lines = f.readlines()
                    same_line = 0
                    orphan_line_1 = 0
                    orphan_line_2 = 0
                    difference_line = 0
                    for line in lines:
                        # print(lines)
                        t = line.split(" ")[0]
                        if "same line" in line:
                            same_line = int(t)  # changed from same_line = int(line[0])
                        elif "important left orphan line" in line:
                            orphan_line_1 = int(t)
                        elif "important right orphan line" in line:
                            orphan_line_2 = int(t)
                        elif "important difference line" in line:
                            difference_line = int(t)
                    output.write(str(now) + "\n")
                    output.write("first file: " + file_1_path + "\n")
                    output.write("second file: " + file_2_path + "\n")
                    output.write("same line: " + str(same_line) + "\n")
                    output.write("orphan_line_1: " + str(orphan_line_1) + "\n")
                    output.write("orphan_line_2: " + str(orphan_line_2) + "\n")
                    output.write("difference_line: " + str(difference_line) + "\n")
                    #print(same_line)
                    #print(orphan_line_1)
                    #print(orphan_line_2)
                    #print(difference_line)

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
                    f.close()
                    #print("overlap: " + str(overlap))
                    #print("contained of the first file: " + str(contained_1))
                    #print("contained of the second file: " + str(contained_2))
    print(now)
    output.close()

bug_output.close()
cmd_output.close()
end = time.time()
print(end - start)
