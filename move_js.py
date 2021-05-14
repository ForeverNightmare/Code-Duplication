import os
import shutil


def search(path, keyword, store_list):
    content = os.listdir(path)
    for each in content:
        each_path = path+os.sep+each
        if keyword in each:
            #print(each_path)
            if not os.path.isdir(each_path):
                store_list.append(each_path)
        if os.path.isdir(each_path):
            search(each_path, keyword, store_list)
        '''elif content_search(each_path, keyword):
            #print(each_path)
            store_list.append(each_path)'''


'''def content_search(filepath, keyword):
    f = open(filepath, 'r')
    for line in f:
        if keyword in line:
            f.close()
            return True
    f.close()
    return False'''


#f = open("top-100.txt")
#lines = f.readlines()
#old_path = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_test\\"
#new_path = "C:\\Users\\Night\\Documents\\Code\\Python\\rename_js\\"
old_path = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_pop\\node_modules\\"
new_path = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_pop_rename_js\\"
keywords = ".js"

'''js_list = []
search(path="C:\\Users\\Night\\Documents\\Code\\Python\\npm\\popular\\chalk", keyword=keywords, store_list=js_list)
length = len(js_list)
for i in range(length):
    t = js_list[i]
    k = t.split("\\")
    new_name = "lodash@" + k[-2] + "@" + k[-1]
    rename_t = t.replace(k[-1], new_name)
    #print(rename_t)
    print(rename_t)
    #os.rename(t, rename_t)
    #shutil.move(rename_t, new_path)'''

#for line in lines:
folders = os.listdir(old_path)
for folder in folders:
    print(folder)
    package_path = old_path + folder
    js_list = []
    search(path=package_path, keyword=keywords, store_list=js_list)
    length = len(js_list)
    if length > 0:
        for i in range(length):
            t = js_list[i]
            k = t.split("\\")
            new_name = folder + "@" + k[-2] + "@" + k[-1]
            #rename_t = t.replace(k[-1], new_name)
            rename_t = t.rstrip(k[-1]) + new_name
            #print(t)
            #print(rename_t)
            os.rename(t, rename_t)
            #shutil.move(rename_t, new_path)
            print(new_path + new_name)
            if not os.path.exists(new_path + new_name):
                shutil.move(rename_t, new_path)
#search(os.getcwd(), input('Your Keyword:'))