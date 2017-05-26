def zoek_grootste_lengte(dict_koppel):
    lengte = 0
    for i in dict_koppel.values():
        if len(i) > lengte:
            lengte = len(i)
    return lengte



def maak_dictionary():
    dict_koppel = {}  # genid:[a1,a2,a3,b1,b2,b3]
    file2 = open("Interactions_relation.data.txt", "r")
    lijst_file2 = file2.readlines()
    file2.close()
    for i in lijst_file2:
        if i.split(",")[3] != "?.\r\n":
            if float(i.split(",")[3].rstrip(".\r\n"))>0.6 and i.split(",")[0] !=i.split(",")[1]:
                try:
                    dict_koppel[i.split(",")[1]] += [[i.split(",")[0],i.split(",")[2],i.split(",")[3]]]
                except KeyError:
                    dict_koppel[i.split(",")[1]] = [[i.split(",")[0], i.split(",")[2], i.split(",")[3]]]
                try:
                    dict_koppel[i.split(",")[0]] += [i.split(",")[1:4]]
                except KeyError:
                    dict_koppel[i.split(",")[0]] = [i.split(",")[1:4]]
    return dict_koppel

def maak_header(lengte):
    header = "GeneID,Essential,Class,Complex,Phenotype,Motif,Chromosome,Function,Localization"
    for i in range(1,lengte+1):
        header +=",GenID"+str(i)+",Type"+str(i)+",Expression_Corr"+str(i)
    header += "\n"
    return header


def toevoegen_aan_file(dict_koppel,lengte):
    file1 = open("Genes_relation.data.txt", "r")
    file3 = open("nieuw file", "w")
    file3.write(maak_header(lengte))
    for regel in file1.readlines():
        if regel.split(",")[0] in dict_koppel.keys():
            regel = regel.rstrip("\r\n").rstrip("\n\r").rstrip("\r").rstrip("\n")
            lijst = dict_koppel[regel.split(",")[0]]
            for x in range(len(lijst)):
                regel+= ","
                regel += lijst[x][0] +","
                regel += lijst[x][1] + ","
                regel += lijst[x][2].rstrip("\r\n").rstrip("\n\r").rstrip("\r").rstrip("\n")
            Nee_waarde = (lengte - len(lijst))*3
            for K in range(Nee_waarde):
                regel += ",NEE"
            regel += "\n"
            file3.write(regel)
        else:
            regel = regel.rstrip("\r\n").rstrip("\n\r").rstrip("\r").rstrip("\n")
            regel += ",NEE"*(lengte*3)
            regel += "\n"
            file3.write(regel)
    file3.close()
    file1.close()



def main():
    dict_koppel = maak_dictionary()
    lengte = zoek_grootste_lengte(dict_koppel)
    print lengte
    toevoegen_aan_file(dict_koppel,lengte)
main()
