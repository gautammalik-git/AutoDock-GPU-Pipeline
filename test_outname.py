import os
import glob
import sys

path = os.getcwd()
names = os.listdir()
prot = "7k15.pdb"
list_dir = []
list_atm = []
lig_dlg = glob.glob(path  + "/*.dlg")

for items in lig_dlg:
    split = items.split("/")
    new_ite = split[-1]
    new_file = prot[:4]+"_" + new_ite[:-4] + ".pdb"
    print(new_file)
    with open(new_file, "w+") as newpdb:
        with open(prot) as g:
            protein = g.readlines()

        for prot_line in protein:
            if (prot_line[:4] == "ATOM"):
                newpdb.write(F'{prot_line}')
       
       
       
        list = []
        with open(new_ite) as f:
            data = f.readlines()
        for linenum, line in enumerate(data):
            if "Num" in line[34:40]:
                line_num = linenum
                next_line = linenum + 4
            if "RMSD TABLE" in line:
                dat = linenum - 3
        with open(new_ite) as f:
            data1 = f.readlines()[next_line:dat]
            list_1 = []
        for lines in data1:
            list_1.append(lines)
        list2 = []
        for items in list_1:
            nex = items[36:40].strip()
            nex = int(nex)
            list2.append(nex)
        for items in list_1:
            if str(max(list2)) in items[36:40]:
                nrun = int(F'{items[19:22].strip()}')
                #print(nrun)
                new_line = F'DOCKED: USER    Run = {nrun}'
                next_new = F'DOCKED: USER    Run = {nrun + 1}'

        for linenum1, line in enumerate(data):
            if new_line == line.strip():
                no_1 = linenum1
                #print(line)
            if next_new == line.strip():
                no_2 = linenum1
                #print(line)
           	

        with open(new_ite) as file:
            #print(new_ite)
            data2 = file.readlines()[no_1:no_2]
            #print((data2))

            for final_lines in data2:
                if "HETATM" in final_lines:
                    next_line1 = F'{final_lines}'
                    #print(next_line1)
                    # print(next_line1)
                    newpdb.write(F'{next_line1[8:-4]} \n')
                elif "ATOM" in final_lines:
                    next_line1 = F'{final_lines[8:-4]} \n'
                    #print(next_line1)
                    newpdb.write(next_line1.replace('ATOM  ', 'HETATM'))








