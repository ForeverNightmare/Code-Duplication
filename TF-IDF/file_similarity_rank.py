import os


class_path = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_projects\\82-processed\\"
report_path = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_projects\\diff\\"
similarity_path = "C:\\Users\\Night\\Documents\\Code\\Python\\npm_projects\\similarity\\"
folders = os.listdir(class_path)

for folder in folders:
    folder_path = class_path + folder + "\\"
    if os.path.isdir(folder_path):
        #print(folder_path)
        report = report_path + folder + "_report.txt"
        similarity_class_path = similarity_path + folder + "\\"
        if not os.path.exists(similarity_class_path):
            os.makedirs(similarity_class_path)
        print(report)
        f = open(report)
        lines = f.readlines()
        similarity_1 = similarity_class_path + "similarity_1.txt"
        similarity_2 = similarity_class_path + "similarity_08_1.txt"
        similarity_3 = similarity_class_path + "similarity_05_08.txt"
        similarity_4 = similarity_class_path + "similarity_02_5.txt"
        similarity_5 = similarity_class_path + "similarity_00_02.txt"
        similarity_6 = similarity_class_path + "similarity_0.txt"

        similarity_1_output = open(similarity_1, 'w', encoding='UTF-8')
        similarity_2_output = open(similarity_2, 'w', encoding='UTF-8')
        similarity_3_output = open(similarity_3, 'w', encoding='UTF-8')
        similarity_4_output = open(similarity_4, 'w', encoding='UTF-8')
        similarity_5_output = open(similarity_5, 'w', encoding='UTF-8')
        similarity_6_output = open(similarity_6, 'w', encoding='UTF-8')
        f.close()
        for line in lines:
            if line.startswith("first file"):
                first_file = line
            elif line.startswith("second file"):
                second_file = line
            elif line.startswith("overlap"):
                t = line.split(": ")[1]
                similarity = float(t)
                if similarity == 1:
                    similarity_1_output.write(first_file)
                    similarity_1_output.write(second_file)
                    similarity_1_output.write(line)
                    similarity_1_output.write("\n")
                elif 0.8 <= similarity < 1:
                    similarity_2_output.write(first_file)
                    similarity_2_output.write(second_file)
                    similarity_2_output.write(line)
                    similarity_2_output.write("\n")
                elif 0.5 <= similarity < 0.8:
                    similarity_3_output.write(first_file)
                    similarity_3_output.write(second_file)
                    similarity_3_output.write(line)
                    similarity_3_output.write("\n")
                elif 0.2 <= similarity < 0.5:
                    similarity_4_output.write(first_file)
                    similarity_4_output.write(second_file)
                    similarity_4_output.write(line)
                    similarity_4_output.write("\n")
                elif 0 < similarity < 0.2:
                    similarity_5_output.write(first_file)
                    similarity_5_output.write(second_file)
                    similarity_5_output.write(line)
                    similarity_5_output.write("\n")
                elif similarity == 0:
                    similarity_6_output.write(first_file)
                    similarity_6_output.write(second_file)
                    similarity_6_output.write(line)
                    similarity_6_output.write("\n")
        similarity_1_output.close()
        similarity_2_output.close()
        similarity_3_output.close()
        similarity_4_output.close()
        similarity_5_output.close()
        similarity_6_output.close()
