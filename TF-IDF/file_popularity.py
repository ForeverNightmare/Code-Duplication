import os
import numpy as np


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

popularity_report = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_projects\\project_similarity\\" \
                    "file_popularity_report.txt"

output = open(popularity_report, 'w', encoding='UTF-8')
for folder in folders:
    folder_path = class_path + folder + "\\"
    if os.path.isdir(folder_path):
        report = report_path + folder + "_report.txt"
        f = open(report)
        lines = f.readlines()
        f.close()
        first_file = " "
        accum_similarity = 0
        max_accum_similarity = -1
        most_popular_file = " "
        for line in lines:
            if line.startswith("first file"):
                now_file = line.split("\\")[-1]
                if now_file != first_file:
                    if accum_similarity > max_accum_similarity:
                        max_accum_similarity = accum_similarity
                        most_popular_file = first_file
                    first_file = now_file
                    accum_similarity = 0
            elif line.startswith("overlap"):
                t = line.split(": ")[1]
                similarity = float(t)
                accum_similarity += similarity
        output.write(folder + "\n")
        output.write(most_popular_file + "\n")

output.close()


