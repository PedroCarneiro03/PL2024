import re
import sys


ativo=True
sum=0


fich=[]

for linha in sys.stdin:
    fich.append(linha)

string_unica = "".join(fich)

for i,on,off,equi,skip,unk in re.findall(r"([\+|-]?\d+)|(on)|(off)|(=)|(\s+)|(.)",string_unica,re.I):

    if equi : print("Resultado Acumulado= ", sum)
    elif on : ativo=True
    elif off : ativo=False
    elif i and ativo : 
        sum += int(i)

