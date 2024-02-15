


f= open("emd.csv")

modalidades=[]
nAptos=0
nInaptos=0

tamanho=20
escalaoEtario=[0]*tamanho ##Nenhum atleta com idade superior a 100
i=0
l1=False
for linha in f:
    if l1:
        campos= linha.split(",")
        for campo in campos:
            if i==8 and campo not in modalidades : #Modalidades
                modalidades.append(campo)

            if i==12: #Resultado
                if campos[i]=="true\n":
                    nAptos+=1
                else:
                    nInaptos+=1
                        
            if i==5: #Idade
                escalaoEtario[int(campo)//5]+=1
            i+=1
        i=0
    else:
        l1=True


modalidades.sort()
totalAtletas= nAptos + nInaptos
percentagemApto=nAptos/totalAtletas * 100
percentagemInapto=nInaptos/totalAtletas * 100



print("Todas as modalidades odernadas alfabeticamente: " + str(modalidades))
print("Percentagem de atletas Aptos: " + str(percentagemApto) + "%  |  Percentagem de atletas Inaptos: " + str(percentagemInapto) + "%")

print("Distribuicao de atltas por escalao etario: ")
for i in range(0,tamanho):
    res=f"""[{i*5}-{i*5+4}]: {escalaoEtario[i]/totalAtletas}%"""
    print(res)

