import os


report_package = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_diff\\"
file_analysis_package = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_file_level_1.0\\"

files = os.listdir(report_package)
files.sort(key=lambda x: int(x[:-11]))
file_list = []
value_list = []
all_file_list = []
all_file_pair_list = []
for file in files:
    #print(file_list)
    #print(value_list)
    report = report_package + file
    print(report)
    f = open(report)
    analysis_file = file.replace("report", "file_level")
    output = open(file_analysis_package + analysis_file, "w")
    lines = f.readlines()
    file_list = []
    value_list = []
    flag = 0
    for line in lines:
        if line.startswith("first file:"):
            first_file = line.split("\\")[-1].replace("\n", '')
            if first_file not in file_list:
                file_list.append(first_file)
                value_list.append(0)
            if first_file not in all_file_list:
                all_file_list.append(first_file)
                all_file_pair_list.append(0)
        if line.startswith("second file:"):
            second_file = line.split("\\")[-1].replace("\n", '')
            if second_file not in file_list:
                file_list.append(second_file)
                value_list.append(0)
            if second_file not in all_file_list:
                all_file_list.append(second_file)
                all_file_pair_list.append(0)
        if line.startswith("overlap"):
            overlap = float(line.split(": ")[1].replace("\n", ''))
        if line.startswith("contained of the first file"):
            contain_first = float(line.split(": ")[1].replace("\n", ''))
        if line.startswith("contained of the second file"):
            contain_second = float(line.split(": ")[1].replace("\n", ''))
            flag = 1
        if flag == 1:
            if overlap >= 1 or contain_first >= 1 or contain_second >= 1:
                first_index = file_list.index(first_file)
                second_index = file_list.index(second_file)

                value_list[first_index] += 1
                value_list[second_index] += 1

                first_index = all_file_list.index(first_file)
                second_index = all_file_list.index(second_file)

                all_file_pair_list[first_index] += 1
                all_file_pair_list[second_index] += 1
            flag = 0
    length = len(file_list)
    rank = min(3, length)
    if rank != 0:
        output.write(str(length))
        output.write("\n")
        value_list, file_list = zip(*sorted(zip(value_list, file_list), reverse=True))
        for i in range(rank):
            output.write(file_list[i] + " " + str(value_list[i]) + "\n")
        output.close()

output = open(file_analysis_package + "file_pair_number.txt", "w")

length = len(all_file_list)
#output.write("js file number: " + str(15904) + "\n")
output.write("js file number: " + str(length) + "\n")
at_least_one_file_pair = 0
for j in range(length):
    if all_file_pair_list[j] > 0:
        at_least_one_file_pair += 1
output.write("js file which has at least one file pair: "
             + str(at_least_one_file_pair) + "\n")

output = open(file_analysis_package + "file_pair_distribution.txt", "w")

fifty = 0
forty = 0
thirty = 0
twenty = 0
ten = 0
one = 0
zero = 0

for i in all_file_pair_list:
    if i >= 50:
        fifty += 1
    elif i >= 40:
        forty += 1
    elif i >= 30:
        thirty += 1
    elif i >= 20:
        twenty += 1
    elif i >= 10:
        ten += 1
    elif i >= 1:
        one += 1
    elif i == 0:
        zero += 1

output.write("50+: " + str(fifty) + "\n")
output.write("40-49: " + str(forty) + "\n")
output.write("30-39: " + str(thirty) + "\n")
output.write("20-29: " + str(twenty) + "\n")
output.write("10-19: " + str(ten) + "\n")
output.write("1-9: " + str(one) + "\n")

















#output.write("0: " + str(zero+7668) + "\n")





