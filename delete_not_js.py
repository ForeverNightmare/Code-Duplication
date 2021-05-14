import os
n = 0
for root, dirs, files in os.walk('C:\\Users\\Night\\Documents\\Code\\Python\\npm_12_pop\\node_modules'):
    for name in files:
        if(not name.endswith(".js")):
            n += 1
            os.remove(os.path.join(root, name))