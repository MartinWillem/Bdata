import re

def functie_1(super_lijst,header):
    super_file = open("uber_file","w")
    super_file.write(header)
    file1 = open("Genes_relation.data.txt","r")
    regels = file1.readlines()
    file1.close()


    eerste_gen = regels[0]
    print eerste_gen
    PATTERN = re.compile(r'''((?:[^,"']|"[^"]*"|'[^']*')+)''')
    eerste_gen = PATTERN.split(eerste_gen)[1::2]
    lijst_van_al = [[],[],[],[],[],[],[],[],[]]
    for x in regels:
        a = PATTERN.split(x)[1::2]
        if eerste_gen[0] != x.split(",")[0]:
            toevoeg_string = eerste_gen[0]
            for G in range(1, 9):
                for T in  super_lijst[G]:
                    if T in lijst_van_al[G]:
                        toevoeg_string += ",True"
                    elif lijst_van_al[G][0] == "?":
                 #       print lijst_van_al[G][0]
                        toevoeg_string += ",?"
                    else:
                        toevoeg_string += ",False"
            toevoeg_string += "\n"
            super_file.write(toevoeg_string)
            eerste_gen = a
            lijst_van_al = [[],[], [], [], [], [], [], [], []]
        for i in range(0, 9):
            lijst_van_al[i].append(a[i].rstrip('.\r\n'))
            lijst_van_al[i] = list(set(lijst_van_al[i]))
    super_file.close()


def header1():
    with open('Genes_relation.names.txt','rw') as file:
        lijst = []
        super_lijst = []
        lijst2 = []
        for line in file:
            if not line.isspace():
                line = line.rstrip("\n ")
                lijst.append(line.split("\r")[0])
        for x in range(0, len(lijst)):
            lijst[x] = re.sub(r'.*:', '', lijst[x])
            lijst[x] = re.sub(r'\.', ',', lijst[x])
            lijst[x] = lijst[x].rstrip(",")
            lijst[x] = lijst[x].strip("\t")
            lijst_klein = []
            for ding in lijst[x].split(","):
                lijst_klein.append(re.sub("\"", "", ding).strip(" "))
            super_lijst.append(lijst_klein)
    return(super_lijst)

def leuke_header_maken(super_lijst) :
    string_header = ""
    for i in range(len(super_lijst)):
        for x in super_lijst[i]:
            string_header +=  x+","
    string_header.rstrip(",")
    string_header += "\n"
    return string_header





def main():
    super_lijst = header1()
    header =leuke_header_maken(super_lijst)
    functie_1(super_lijst,header)
main()
