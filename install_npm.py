import os
import shutil
f = open("sum_result_pop_1440.txt")

lines = f.readlines()

project_path = r"\\?\{}".format("C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_pop\\node_modules\\")
install_path = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_2\\node_modules\\"
for line in lines:
    project = line.replace("\n", "")

    real_project_name = project
    if project.startswith("@") and r"/" in project:
        prefix = project.split(r"/")[0]
        suffix = project.split(r"/")[1]
        real_project_name = prefix + "#" + suffix

    if not os.path.isdir(project_path + real_project_name):
        # and not project.startswith("@")
        k = "npm i " + project
        command = "cd C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_2 & " + k
        print(command)
        os.system(command)

        if project.startswith("@") and r"/" in project:
            prefix = project.split(r"/")[0]
            suffix = project.split(r"/")[1]
            #print(prefix)
            #print(suffix)
            install_path_individual = install_path + prefix + "\\" + suffix + "\\"

            if os.path.exists(install_path_individual):
                new_name = prefix + "#" + suffix
                t = install_path + prefix + "\\" + new_name + "\\"
                os.rename(install_path_individual, t)
                install_path_individual = t

                install_path_individual = r"\\?\{}".format(install_path_individual)
                for root, dirs, files in os.walk(install_path_individual):
                    for name in files:
                        if not name.endswith(".js"):
                            os.remove(os.path.join(root, name))

                new_path = project_path + new_name + "\\"

                if not os.path.exists(new_path):
                    shutil.move(install_path_individual, project_path)
        else:
            install_path_individual = install_path + project + "\\"
            install_path_individual = r"\\?\{}".format(install_path_individual)
            if os.path.exists(install_path_individual):

                for root, dirs, files in os.walk(install_path_individual):
                    for name in files:
                        if not name.endswith(".js"):
                            os.remove(os.path.join(root, name))

                new_path = project_path + project + "\\"
                if not os.path.exists(new_path):
                    shutil.move(install_path_individual, project_path)

        final_path = r"\\?\{}".format("C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_2\\node_modules\\")
        shutil.rmtree(r"C:\Users\Night\AppData\Roaming\npm-cache")
        if os.path.isdir(final_path):
            shutil.rmtree(final_path)
        if os.path.exists(r"C:\Users\Night\Documents\Code\Python\npm_12_2\package-lock.json"):
            os.remove(r"C:\Users\Night\Documents\Code\Python\npm_12_2\package-lock.json")
