import numpy as np
import os

class_file = open("C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_predict\\class.txt")
parameter = 1.0
lines = class_file.readlines()

package_list = []
class_list = []
for line in lines:
    t = line.replace("\n", "").split(" ")
    package_list.append(t[0])
    class_list.append(int(t[1]))

#print(package_list)
#print(class_list)

package_number = len(package_list)
class_number = [0] * 12
for i in range(package_number):
    class_number[class_list[i]] += 1

#print(class_number)

similarity_matrix = np.zeros((package_number, package_number))

print(similarity_matrix)

report_folder = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_diff\\"
files = os.listdir(report_folder)
files.sort(key=lambda x: int(x[:-11]))

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
        if line.startswith("second file:"):
            second_file = line.split("\\")[-1].replace("\n", '')
            if second_file.startswith("@"):
                second_package = "@" + second_file.split("@")[1]
            else:
                second_package = second_file.split("@")[0]
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

                similarity_matrix[first_index, second_index] += 1
                similarity_matrix[second_index, first_index] += 1
            flag = 0

class_matrix = np.zeros((package_number, 12))
similar_package_list = []
for i in range(package_number):
    for j in range(package_number):
        if similarity_matrix[i, j] >= 3:
            if package_list[i] not in similar_package_list:
                similar_package_list.append(package_list[i])
            if package_list[j] not in similar_package_list:
                similar_package_list.append(package_list[j])
package_analysis_folder = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_package_level_1.0\\"

output = open(package_analysis_folder + "package_analysis_4.txt", "w")
similar_package_number = {}
for i in range(package_number):
    for j in range(package_number):
        if similarity_matrix[i, j] >= 3:
            if package_list[i] in similar_package_number.keys():
                similar_package_number[package_list[i]] += 1
            else:
                similar_package_number[package_list[i]] = 1

            if package_list[j] in similar_package_number.keys():
                similar_package_number[package_list[j]] += 1
            else:
                similar_package_number[package_list[j]] = 1
similar_package_number_list = sorted(similar_package_number.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)

for p in range(50):
    t = similar_package_number_list[p][0]
    output.write(t + "\n")

    index = package_list.index(t)
    print(index)
    first = -1
    second = -2
    third = -3
    first_package = ""
    second_package = ""
    third_package = ""
    for j in range(package_number):
        if similarity_matrix[index, j] >= 3:
            k = similarity_matrix[index, j]
            if k >= first:
                third = second
                third_package = second_package
                second = first
                second_package = first_package
                first = k
                first_package = package_list[j]
            elif first > k >= second:
                third = second
                third_package = second_package
                second = k
                second_package = package_list[j]
            elif second > k >= third:
                third = k
                third_package = package_list[j]
    output.write("most similar package: \n")
    output.write("1: " + first_package + "\n")
    output.write("2: " + second_package + "\n")
    output.write("3: " + third_package + "\n")
    output.write("\n")


