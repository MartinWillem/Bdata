import re
def header1():
    with open('Genes_relation.names.txt','rw') as file:
        lijst = []
        lijst2 = []
        for line in file:
            if not line.isspace():
                line = line.rstrip("\n ")
                lijst.append(line.split("\r")[0])
        print lijst
        for x in range(0, len(lijst)):
            lijst[x] = re.sub(r'.*:', '', lijst[x])
            lijst[x] = re.sub(r'\.', ',', lijst[x])
            lijst[x] = lijst[x].rstrip(",")
            lijst[x] = lijst[x].strip("\t")
            string = ""
            for ding in lijst[x].split(","):
                lijst2.append([re.sub("\"", "", ding).strip(" ")])
    return lijst

header1()