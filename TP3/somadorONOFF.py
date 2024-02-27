import re
import sys

onregex= r"(?i)on"
offregex= r"(?i)off"
intregex= r"[\+\-]?\d+"

ativo=False
sum=0

for linha in sys.stdin:

    for palavra in linha.split():
        if(re.match(onregex,palavra)):
            ativo=True
        if(re.match(offregex,palavra)):
            ativo=False
        if(re.match(intregex,palavra)):   
            if(ativo==True):
                sum+=int(palavra)
        if(palavra=="="):
            print("Resultado da soma ate ao momento: " + str(sum))

