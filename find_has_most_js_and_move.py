import os
import shutil

dirnum = 0
filenum = 0
project_path = 'C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_pop\\node_modules\\'
new_path = 'C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_most_and_less\\'
folders = os.listdir(project_path)
tototal = 0

folder_file = {}
for folder in folders:
    total = 0
    package_path = project_path + folder + "\\"
    for dirpath, dirnames, filenames in os.walk(package_path):
            file_count = 0
            for file in filenames:
                file_count = file_count + 1
            #print(dirpath,file_count)
            total = total + file_count

    print(folder)
    print(total)
    folder_file[folder] = total
    tototal = tototal + total

folder_file_rank = sorted(folder_file.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
print(folder_file_rank)
print(tototal)

'''for i in range(100):
    old_folder = project_path + folder_file_rank[i][0]
    new_folder = new_path + folder_file_rank[i][0]
    if os.path.isdir(old_folder) and not os.path.isdir(new_folder):
        shutil.move(old_folder, new_path)

    old_folder = project_path + folder_file_rank[-1 * i - 1][0]
    new_folder = new_path + folder_file_rank[-1 * i - 1][0]
    if os.path.isdir(old_folder) and not os.path.isdir(new_folder):
        shutil.move(old_folder, new_path)'''
