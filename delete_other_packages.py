import os
import shutil


project_path = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_2\\node_modules\\"

f = open("sum_result.txt")

lines = f.readlines()
project_list = []
now = 0
for line in lines:
    now += 1
    project_list.append(line[0:-1])

folders = os.listdir(project_path)

for folder in folders:
    if folder not in project_list:
        shutil.rmtree(project_path + folder)



