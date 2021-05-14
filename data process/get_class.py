import os

class_file = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_projects\\sum_result.txt"

f = open(class_file)

lines = f.readlines()

original_package_list = []
original_class_list = []
now = 0
now_class = 0
for line in lines:
    now += 1
    original_package_list.append(line.replace("\n", '').replace("/", "#"))
    original_class_list.append(now_class)
    if now % 120 == 0:
        now_class += 1


report_folder = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_diff\\"
files = os.listdir(report_folder)
files.sort(key=lambda x: int(x[:-11]))
package_list = []

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
        if line.startswith("second file:"):
            second_file = line.split("\\")[-1].replace("\n", '')
            if second_file.startswith("@"):
                second_package = "@" + second_file.split("@")[1]
            else:
                second_package = second_file.split("@")[0]
            if second_package not in package_list:
                package_list.append(second_package)

class_list = []
for i in range(len(package_list)):
    index = original_package_list.index(package_list[i])
    class_list.append(original_class_list[index])

output = open("C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_predict\\class.txt", "w")
for i in range(len(package_list)):
    output.write(package_list[i] + " " + str(class_list[i]) + "\n")
