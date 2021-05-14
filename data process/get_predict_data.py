import numpy as np
import os

class_file = open("C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_predict\\class.txt")

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
            if overlap > 0.2 or contain_first > 0.2 or contain_second > 0.2:
                first_index = package_list.index(first_package)
                second_index = package_list.index(second_package)

                similarity_matrix[first_index, second_index] += 1
                similarity_matrix[second_index, first_index] += 1
            flag = 0

output = open("C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_predict\\similarity_matrtix.txt", "w")
for i in range(package_number):
    output.write(package_list[i] + "\n")
    for j in range(package_number):
        output.write(str(similarity_matrix[i, j]) + " ")
    output.write("\n")
output.close()

class_matrix = np.zeros((package_number, 12))
for i in range(package_number):
    for j in range(package_number):
        if similarity_matrix[i, j] >= 3:
           class_matrix[i, class_list[j]] += 1

output = open("C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_predict\\similarity_class_matrtix.txt", "w")
for i in range(package_number):
    output.write(package_list[i] + " " + str(class_list[i]) + "\n")
    for j in range(12):
        output.write(str(class_matrix[i, j] / class_number[j] * 100) + " ")
    output.write("\n")
output.close()
