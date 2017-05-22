import os
import re

def main():
    dict_koppel = {} # genid:[a1,a2,a3,b1,b2,b3]
    hoogste_aantal = int(os.popen("""cat Genes_relation.data.txt | awk -F "," '{print $1}'|uniq -c|sort| awk '{print $1}' | head -n1""").read().rstrip("\n"))
    file1 = open("Genes_relation.data.txt","r")
    lijst_file1 = file1.readlines()
    file1.close()
    file2 = open("Interactions_relation.data.txt","r")
    lijst_file2 = file2.readlines()
    file2.close()
    file4 = open("Genes_relation.names.txt","r")
    lijst_file4 = file4.readlines()
    file4.close()
    for i in lijst_file2:
        try:
            dict_koppel[i.split(",")[0]] += [i.split(",")[1:4]]
        except KeyError:
            dict_koppel[i.split(",")[0]] = [i.split(",")[1:4]]
    file3 = open("nieuw file","w")
##    for a,b in dict_koppel.items():
##        for i in lijst_file1:
##            if i.split(",")[0]== a:
##                for lijsten in b:
##                    toevoeg_regels = i.rstrip("\n")
##                    for gegevens in lijsten:
##                        toevoeg_regels +=","+gegevens
##                    file3.write(toevoeg_regels)
##                file3.write(i.rstrip("\n")+",[]"*(hoogste_aantal-(len(b))*3)+"\n")
    keys = dict_koppel.keys()
    header = ""
    for x in lijst_file4:
        if re.search(".*\:", x) != None:
            header += (re.search(".*\:", x).group()).rstrip(":") + ","
    header = header.rstrip(",")
    cijfer = 0
    for x in range(0, hoogste_aantal):
        cijfer += 1
        header += ",Interactie_" + str(cijfer) + ", Interactie_" + str(cijfer) + "-type" + ",Interactie_" + str(cijfer) + "-Coefficient"
    header += "\n"
    file3.write(header) #bovenaantoevoegen
    print header
    for i in lijst_file1:
        if i.split(",")[0] in keys:
            regel = i.rstrip("\n").lstrip("\n").rstrip("\r\n").rstrip("\r")
            for lijsten in dict_koppel[i.split(",")[0]]:
                regel += ","
                regel += ",".join(lijsten).rstrip("\r\n").rstrip("\r")
            for x in range((hoogste_aantal -len(dict_koppel[i.split(",")[0]]))*3):
                regel += ",?"
            regel += "\n"
            file3.write(regel)
        else:
            regel = i.rstrip("\n").lstrip("\n").rstrip("\r\n").rstrip("\r")
            for t in range(hoogste_aantal*3):
                regel+=",?"
            regel +="\n"
            regel = regel
            file3.write(regel)

        filecompleet = open("nieuw file", "r")
        data = filecompleet.readlines()
        for x in data:
            regel = []
            if re.search(",\d,", x) != None:
                regel.append(re.search(",*\d*.,", x).group(0))
        print regel



            
##       for a,b in dict_koppel.items():
##            print()
##           # print(i.split(",")[0])
##           # print(i.split(",")[0])
##            if i.split(",")[0].rstrip("\n")== a.rstrip("\n"):
##                voorkomen = True
##                toevoeg_regels = "\n"+i.rstrip("\n")
##                for lijsten in b:
##                    for gegevens in lijsten:
##                        joep = ","+gegevens.rstrip("\n")
##                        toevoeg_regels += (joep)
##                file3.write(toevoeg_regels)
##        if voorkomen == False:
##            file3.write(i.rstrip("\n")+",[]"*(hoogste_aantal-(len(b))*3)+"\n")
##   file3.close()
        
                
 

        
#-----------------------------------------------
##    for i in lijst_file2:
##        try:
##            dict_koppel[i.split(",")[1]] += [i.split(",")[0]+","+i.split(",")[2]+","+i.split(",")[3]]
##        except KeyError:
##            dict_koppel[i.split(",")[1]] = [i.split(",")[0]+","+i.split(",")[2]+","+i.split(",")[3]]
##    for a,b in dict_koppel.items():
##        print(a,"\t",b)





main()
