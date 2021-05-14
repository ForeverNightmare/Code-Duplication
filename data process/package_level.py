import os


report_folder = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_diff\\"
package_analysis_folder = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_package_level_1.0\\"
parameter = 1.0
files = os.listdir(report_folder)
files.sort(key=lambda x: int(x[:-11]))
package_list = []
value_list = []
for file in files:
    #print(file_list)
    #print(value_list)
    report = report_folder + file
    print(report)
    f = open(report)
    lines = f.readlines()
    flag = 0
    for line in lines:
        if line.startswith("first file:"):
            first_file = line.split("\\")[-1].replace("\n", '')
            if first_file.startswith("@"):
                first_package = "@" + first_file.split("@")[1]
            else:
                first_package = first_file.split("@")[0]
            #print(first_package)
            if first_package not in package_list:
                package_list.append(first_package)
                value_list.append(0)
        if line.startswith("second file:"):
            second_file = line.split("\\")[-1].replace("\n", '')
            if second_file.startswith("@"):
                second_package = "@" + second_file.split("@")[1]
            else:
                second_package = second_file.split("@")[0]
            if second_package not in package_list:
                package_list.append(second_package)
                value_list.append(0)
            #print(second_package)
        if line.startswith("overlap"):
            overlap = float(line.split(": ")[1].replace("\n", ''))
        if line.startswith("contained of the first file"):
            contain_first = float(line.split(": ")[1].replace("\n", ''))
        if line.startswith("contained of the second file"):
            contain_second = float(line.split(": ")[1].replace("\n", ''))
            flag = 1
        if flag == 1:
            if overlap >= parameter or contain_first >= parameter or contain_second >= parameter:
                first_index = package_list.index(first_package)
                second_index = package_list.index(second_package)

                value_list[first_index] += 1
                value_list[second_index] += 1
            flag = 0

output = open(package_analysis_folder + "package_analysis.txt", "w")
length = len(package_list)
#output.write(str(length))
#output.write("\n")
value_list, package_list = zip(*sorted(zip(value_list, package_list), reverse=True))
for i in range(50):
    output.write(package_list[i] + " " + str(value_list[i]) + "\n")
output.close()
