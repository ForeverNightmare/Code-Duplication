import os
import numpy as np


def get_key(dict, value):
    return [k for k, v in dict.items() if v == value]

project_path = "C:\\Users\\Night\\Documents\\Code\\Python\\npm\\popular"
project_dict = {}

folders = os.listdir(project_path)
length = len(folders)
now = -1
for folder in folders:
    now += 1
    project_dict[folder] = now

project_similarity = np.zeros((length, length))
class_path = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_projects\\82-processed\\"
report_path = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_projects\\diff\\"
folders = os.listdir(class_path)
for folder in folders:
    folder_path = class_path + folder + "\\"
    if os.path.isdir(folder_path):
        report = report_path + folder + "_report.txt"
        f = open(report)
        lines = f.readlines()
        f.close()
        max_similarity = -1
        first_file = " "
        final_second_file = " "
        for line in lines:
            if line.startswith("first file"):
                now_file = line.split("\\")[-1]
                if now_file != first_file and first_file != " ":
                    first_project = first_file.split("@")[0]
                    second_project = final_second_file.split("@")[0]
                    first_project_index = project_dict[first_project]
                    second_project_index = project_dict[second_project]
                    project_similarity[first_project_index][second_project_index] += max_similarity
                    first_file = now_file
                    max_similarity = -1
                elif now_file != first_file and first_file == " ":
                    first_file = now_file
                    max_similarity = -1
                #print(first_file)
            elif line.startswith("second file"):
                second_file = line.split("\\")[-1]
                #print(second_file)
            elif line.startswith("overlap"):
                t = line.split(": ")[1]
                similarity = float(t)
                if similarity > max_similarity:
                    final_second_file = second_file
                    max_similarity = similarity
#print(project_similarity)

similarity_report = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_projects\\project_similarity\\" \
                    "project_similarity_report.txt"

output = open(similarity_report, 'w', encoding='UTF-8')
for i in range(length):
    max_project_similarity = -1
    most_similar_project = 0
    for j in range(i+1, length):
        if project_similarity[i, j] > max_project_similarity:
            max_project_similarity = project_similarity[i, j]
            most_similar_project = j
    project_1 = get_key(project_dict, i)
    project_2 = get_key(project_dict, most_similar_project)

    output.write(str(project_1) + "\n")
    output.write(str(project_2) + "\n")
    output.write("\n")
output.close()
