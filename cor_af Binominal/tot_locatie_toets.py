import os
import re




def super_lijst_maken():
    file1 = open("k-nn_genes_relation.toets.csv", "r")
    alle_regels = file1.readlines()
    file1.close()
    PATTERN = re.compile(r'''((?:[^,"']|"[^"]*"|'[^']*')+)''')
    super_lijst = [[], [], [], [], [], [], [], []]
    for regel in alle_regels:
        gesplitte_regel = PATTERN.split(regel.rstrip(".\r\n"))[1::2]
        for i in range(0, 8):
            if gesplitte_regel[i] != "?" and gesplitte_regel[i] != "Unknown":
                super_lijst[i].append(gesplitte_regel[i])
                super_lijst[i] = list(set(super_lijst[i]))
    super_lijst[0] = ["label"]
    super_lijst[-1] = ["locatie"]
    print len(super_lijst)
    print repr(super_lijst[0])
    print repr(super_lijst[1])
    print repr(super_lijst[2])
    print repr(super_lijst[3])
    print repr(super_lijst[4])
    print repr(super_lijst[5])
    print repr(super_lijst[6])
    print repr(super_lijst[7])
    return super_lijst

def leuke_header_maken(super_lijst) :
    string_header = ""
    for i in range(len(super_lijst)-1):
        for x in super_lijst[i]:
            string_header += "\'" +x+"\'"+","
    string_header += "locatie,"
    string_header = string_header# + string_header2
    string_header = string_header.rstrip(",")
    string_header += "\n"
    print string_header
    return string_header


def functie_1(super_lijst,header):
    file1 = open("k-nn_genes_relation.toets.csv","r")
    alle_regels = file1.readlines()
    file1.close()
    super_file = open("uber_file_totlocatieTEST.csv","w")
    super_file.write(header)
    eerste_gen = alle_regels[0]
    PATTERN = re.compile(r'''((?:[^,"']|"[^"]*"|'[^']*')+)''')
    eerste_gen = PATTERN.split(eerste_gen.rstrip(".\r\n"))[1::2]
    lijst_van_al = [[],[],[],[],[],[],[],[]]
    alle_regels.append(12 * " ,")
    for regel in alle_regels:
        gesplitte_regel = PATTERN.split(regel.rstrip(".\r\n"))[1::2]
        if eerste_gen[0] != regel.split(",")[0]:
            toevoeg_string = eerste_gen[0]
            for lijst_nummer in range(1, 7):
                for sl_woord in  super_lijst[lijst_nummer]:
                    for kaas in lijst_van_al[lijst_nummer]:
                        ja = False
                        if sl_woord == kaas:
                            ja = True
                            break
                        elif kaas == "?":
                            ja = "niet_chill"
                            break
                    if ja == True:
                        toevoeg_string += ",True"
                    elif ja == False:
                        toevoeg_string += ",False"
                    else:
                        toevoeg_string += ",?"
            toevoeg_string += ","+lijst_van_al[-1][0].strip("\"").replace(".","")
            toevoeg_string += "\n"
            super_file.write(toevoeg_string)
            eerste_gen = gesplitte_regel
            lijst_van_al = [[],[], [], [], [], [], [], []]
        for i in range(0, 8):
            lijst_van_al[i].append(gesplitte_regel[i])
            lijst_van_al[i] = list(set(lijst_van_al[i]))
    super_file.close()




def main():
    super_lijst = super_lijst_maken()
    header = leuke_header_maken(super_lijst)
    functie_1(super_lijst,header)


main()
