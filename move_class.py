import os
import shutil

f = open("best-1130.txt")
file_path = "C:\\Users\\Night\\Documents\\Code\\Python\\rename2\\"
lines = f.readlines()

for line in lines:
    #print(line)
    t = line.replace("\n", "")
    t = t.split(" ")
    #print(len(t))
    if len(t) == 2 and t[0] != "" and t[1] != "":
        class_folder = file_path + t[1]
        if not os.path.exists(class_folder):
            os.makedirs(class_folder)
        file = file_path + t[0]
        if os.path.exists(file):
            shutil.move(file, class_folder)
