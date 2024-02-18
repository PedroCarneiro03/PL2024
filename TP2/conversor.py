

import sys,re

bold = r"\*\*([^\*]*)\*\*"
italico= r"\*([^\*]*)\*"
lista=r"1."

for linha in sys.stdin:
    #print(linha)
    bolds = re.findall(bold, linha)
    italicos = re.findall(italico, linha)
    if len(bolds) != 0:
        print("Bolds:" + str(bolds))
    if len(italicos) !=0 :    
        print("Italicos:" + str(italicos))

