import shutil
import os

f = open("sum_result.txt")
lines = f.readlines()
old_path = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_2\\node_modules\\"
new_path = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_pre\\node_modules\\"
#shutil.move("C:\\Users\\Night\\Documents\\Code\\Python\\npm\\node_modules\\chalk",
            #"C:\\Users\\Night\\Documents\\Code\\Python\\npm\\popular")

for line in lines:
    package = line.replace("\n", "")
    old_folder = old_path + package
    new_folder = new_path + package
    #print(old_folder)
    if os.path.isdir(old_folder) and not os.path.isdir(new_folder):
        shutil.move(old_folder, new_path)
