import re

def functie_1(super_lijst,header):
    super_file = open("uber_file","w")
    super_file.write(header)
    file1 = open("Genes_relation.data.txt","r")
    alle_regels = file1.readlines()
    file1.close()
    eerste_gen = alle_regels[0]
    PATTERN = re.compile(r'''((?:[^,"']|"[^"]*"|'[^']*')+)''')
    eerste_gen = PATTERN.split(eerste_gen)[1::2]
    lijst_van_al = [[],[],[],[],[],[],[],[],[]]
    for regel in alle_regels:
        gesplitte_regel = PATTERN.split(regel)[1::2]
        if eerste_gen[0] != regel.split(",")[0]:
            print lijst_van_al
            toevoeg_string = eerste_gen[0]
            for lijst_nummer in range(1, 9):
                for sl_woord in  super_lijst[lijst_nummer]:
                    for kaas in lijst_van_al[lijst_nummer]:
                        if sl_woord == kaas:
                            ja = True
                        elif kaas == "?":
                            ja = False
                        else:
                            ja = "niet_chill"
                    if ja == True:
                        toevoeg_string += ",True"
                    elif ja == False:
                        toevoeg_string += ",?"
                    else:
                        toevoeg_string += ",False"


            toevoeg_string += "\n"
            super_file.write(toevoeg_string)
            eerste_gen = gesplitte_regel
            lijst_van_al = [[],[], [], [], [], [], [], [], []]
        for i in range(0, 9):
            lijst_van_al[i].append(maakschoon(gesplitte_regel[i]))
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
    print repr(string_header)
    string_header = string_header.rstrip(",")
    string_header += "\n"
    return string_header


def maakschoon(niet_schoon):
    niet_schoon = re.sub(",", "", niet_schoon)
    niet_schoon = re.sub(r'(?:_[A-z])?\.([^.]*)$', "", niet_schoon)
    niet_schoon = re.sub('"', "", niet_schoon)
    return niet_schoon


def main():
    super_lijst = header1()
    header =leuke_header_maken(super_lijst)
    functie_1(super_lijst,header)
main()