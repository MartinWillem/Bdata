import re
'''
Belangerijk :haalt de header op van het eerste bestand en voegt de nieuw atributten toe.
Verder wordt elke atribuut die toegevoegd wordt in 'kleine header' opgeslagen.
beide worden gereturned.
'''
def maak_een_nieuwe_header(super_dict):
    file1 = open("uber_file_totlocatieTRAINING.csv","r")
    alle_regeltjes = file1.readlines()
    file1.close()
    header = alle_regeltjes[0]
    header =  "".join(header).rstrip("\n")
    kleine_header = []
    for regel in super_dict.keys():
        header += ",Type "+ regel
        header += ",Interactie " +regel
        kleine_header.append(regel)
    return header,kleine_header

def roep_locatie_file(file):
    file1 = open(file,"r")
    a = file1.readlines()
    file1.close()
    return(a)


'''
De eerder gemaakte 'header' wordt weggeschreven naar het bestand (new_cor_file.csv).

Voor elke regel in 'uber_file_totlocatie.csv', wordt er gelooped.
Voor elk genid in de regel wordt er geloept door 'klein_header' -> dit zijn alle attributen die bij header zijn begevoegd in een lijst.
Er wordt gecheckt of het genid gelijk is aan het gen in de header.
Als dat zo is toelating -> True, anders is het False.
Bij een true worden de gegevens van de connectie aan de regel toegevoegd:
UB_regel += ,Genetic,0.588783454.
Bij een false:
UB_regel += ",False,0"

Als het genid helemaal geen connectie heeft bestaat deze ook niet in de dict.
Dit wordt opgevangen in de try except -> UB_regel+= ",False,0"

Op het einde wordt de regel weggeschreven naar new_cor_file.csv.
'''
def het_vinden_en_toevoegen(super_dict,header,kleine_header):
    file1 = open("new_cor_file_TRAINING_MET_THRESHOLD.csv","w")
    file1.write(header+"\n")

    regels_uit_uber =roep_locatie_file("uber_file_totlocatieTRAINING.csv")
    for UB_regel in regels_uit_uber[1::]:
        UB_regel = UB_regel.rstrip("\n")
        for atribuut in kleine_header:
            try:
                for interactie in super_dict[UB_regel.split(",")[0]]:#.strip("\"")]:
                    toelating = False
                  #  print interactie[0], "\t", atribuut
                    if interactie[0] ==atribuut:
                        toelating = True
                        break
                if toelating==True:
                    UB_regel += "," + interactie[1] + "," + "TRUE"
                else:
                    UB_regel += ",False,0"
            except KeyError:
                UB_regel+= ",False,0"
        file1.write(UB_regel+"\n")
    file1.close()



'''
Deze functie maakt een dictionary, waarin als een key het genid wordt genomen en als value het andere gen samen
met de conf en de fase(?). Zo ziet het eruit
dict_koppel['G234275'] -> [['G235287', 'Physical', '-0.422805819.\r\n'], ['G235439', 'Physical', '-0.347782909.\r\n']]
dict_koppel['G235439'] ->[['G234275', 'Physical', '-0.347782909.\r\n'], ['G235735', 'Physical', '0.317403512.\r\n']]
Zoals te zien is staat het ook 2 kanten.
'''
def maak_dictionary():
    dict_koppel = {}
    file2 = open("k-nn_Interactions_relation.csv", "r")
    lijst_file2 = file2.readlines()
    file2.close()
    for i in lijst_file2:
    #    if i.split(",")[3] != "?.\r\n":
        if float(i.split(",")[3].rstrip(".\r\n")) > 0.6 or float(i.split(",")[3].rstrip(".\r\n")) < -0.6 and i.split(",")[0] != i.split(",")[1]:
            try:
                dict_koppel[i.split(",")[1]] += [[i.split(",")[0], i.split(",")[2], i.split(",")[3]]]
            except KeyError:
                dict_koppel[i.split(",")[1]] = [[i.split(",")[0], i.split(",")[2], i.split(",")[3]]]
            try:
                dict_koppel[i.split(",")[0]] += [i.split(",")[1:4]]
            except KeyError:
                dict_koppel[i.split(",")[0]] = [i.split(",")[1:4]]
    return dict_koppel
'''
Main stuurt alles aan
'''

def main():
    super_dict = maak_dictionary()
    header,kleine_header = maak_een_nieuwe_header(super_dict)
    het_vinden_en_toevoegen(super_dict,header,kleine_header)

main()