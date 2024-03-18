import os
import sys
import glob
path = os.getcwd()
#print(path)
file_path = F'{path}/*.dlg'
#print(file_path)
with open("Energy.txt", "w+") as output:
    file_name = glob.glob(file_path)
    new_list = []
    for items in file_name:
        split_item  = items.split("/")
        new_list.append(split_item[-1])
        new_fi = sorted(new_list)
    for item in new_fi:
        #print(item)
        with open(item) as f:
            data = f.readlines()
            #print(data)
        for linenum, lines in enumerate(data):
            if "Num" in lines[34:40]:
                line_num = linenum
                line_1 = line_num + 4
            if "RMSD TABLE" in lines:
                line_2 = linenum - 3
        with open(item) as f1:
            data1 = f1.readlines()[line_1:line_2]
            #print(data1)
            list = []
        for newline in data1:
            list.append(newline)
        #print(list)
        list2 = []
        for items in list:
            nex = items[36:40].strip()
            nex = int(nex)
            list2.append(nex)
        #print(list2)
        #max = max(list2)
        for items in list:
            if str(max(list2)) in items[36:40]:
               final_energy = (F'{item[:-4]} {items[10:16]} kcal/mol')
               print(final_energy)
               print(F'Conformations: {items[37:40]} \n')
               output.write(F'{final_energy} \n')



