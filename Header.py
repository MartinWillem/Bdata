import re
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
            string = ""
            lijst_klein = []
            for ding in lijst[x].split(","):
                lijst_klein.append(re.sub("\"", "", ding).strip(" "))
                print ding
            print "--------------------"
            super_lijst.append(lijst_klein)
    print len(super_lijst)
    print super_lijst[2]
       # print lijst[4]
 #   print lijst2

header1()
