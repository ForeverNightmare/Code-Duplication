# -*- coding: UTF-8 -*-

import numpy as np
import re

#files = np.empty((10, 10), dtype=np.object)
files = np.empty(20000, dtype=np.object)
f = open("files-stats-0.stats")
lines = f.readlines()

for line in lines:
    t = line.split(",")
    #project_number = int(t[0])
    file_number = int(t[1])
    #print(project_number)
    #print(file_number)
    #print(line.split(','))
    file_name = t[2].replace('"', '').split("\\")[1]
    print(file_name)
    #files[project_number][file_number] = file_name
    files[file_number] = file_name
#print(files)

f = open("files-tokens-0.tokens", encoding='UTF-8')
lines = f.readlines()

output = open("corpus2.txt", 'w', encoding='UTF-8')

keyword = ["abstract", "arguments", "boolean", "break", "byte", "case", "catch", "char", "class*", "const", "continue",
           "debugger", "default", "delete", "do", "double", "else", "enum*", "eval", "export*", "extends*", "false",
           "final", "finally", "float", "for", "function", "goto", "if", "implements", "import*", "in", "instanceof",
           "int", "interface", "let", "long", "native", "new", "null", "package", "private", "protected", "public",
           "return", "short", "static", "super*", "switch", "synchronized", "this", "throw", "throws", "transient",
           "true", "try", "typeof", "var", "void", "volatile", "while", "with", "yield", "Array", "Date", "eval",
           "function", "hasOwnProperty", "Infinity", "isFinite", "isNaN", "isPrototypeOf", "length", "Math", "NaN",
           "name", "Number", "Object", "prototype", "String", "toString", "undefined", "valueOf"]
for line in lines:
    #print(line)
    line = line.replace("\n", '')
    #print(line)
    #project_number = int(line[0])
    t = line.split(",")
    file_number = int(t[1])
    #output.write(files[project_number][file_number])
    output.write(files[file_number])
    t = line.split("@#@")[1]
    if len(t) > 0:
        t = t.split(',')
        for i in range(len(t)):
            tt = t[i].split("@@::@@")
            #if (len)
            word = tt[0]
            word_frequency = int(tt[1])
            if not word.isdigit() and word not in keyword and re.match("^[A-Za-z0-9_-]*$", word):
                for j in range(word_frequency):
                    output.write(" " + word)
    output.write("\n")
    #print(t)
