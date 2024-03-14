import ply.lex as lex
import json
import sys
import re

def printaSaldo():
    if(lexer.euros>=1):
        print("maq: Saldo = "+ str(lexer.euros) + "e"+ str(lexer.centimos)+"c")
    else:
        print("maq: Saldo = " + str(lexer.centimos)+"c")


def encontraProduto(codigo):
    encontrado=None
    for item in stock["stock"]:
        if item["cod"] == codigo:
            encontrado = item
            break
    return encontrado

def eliminaProduto(codigo):
    for item in stock["stock"]:
        if item["cod"] == codigo:
            if(item["quant"] > 0):
                item["quant"]-=1
            else:
                stock["stock"].remove(item)

    with open("stock.json", "w", encoding="utf-8") as arquivo_json:
        json.dump(stock, arquivo_json, indent=4, ensure_ascii=False)

def toStr(n,moeda,tipo):
    #(n1e,"1","e")
    if (n==0):
        return ""
    else:
        return str(n) + "x " + moeda + tipo


# List of token names.   This is always required
tokens = (
    "MOEDA",
    "SELECIONAR",
    "SAIR"
    
)



# Regular expression rules for simple tokens
def t_SAIR(t):
    r"SAIR"
    n1e=0
    while(lexer.euros>0):
        n1e+=1
        lexer.euros-=1
    n50c=0
    while(lexer.centimos>=50):
        n50c+=1
        lexer.centimos-=50
    n20c=0
    while(lexer.centimos>=20):
        n20c+=1
        lexer.centimos-=20
    n10c=0
    while(lexer.centimos>=10):
        n10c+=1
        lexer.centimos-=10
    n5c=0
    while(lexer.centimos>=5):
        n5c+=1
        lexer.centimos-=5
    n2c=0
    while(lexer.centimos>=2):
        n2c+=1
        lexer.centimos-=2
    n1c=0
    while(lexer.centimos>=1):
        n1c+=1
        lexer.centimos-=1
    
    a=toStr(n1e,"1","e")
    b=toStr(n50c,"50","c")
    c=toStr(n20c,"20","c")
    d=toStr(n10c,"10","c")
    e=toStr(n5c,"5","c")
    f=toStr(n2c,"2","c")
    g=toStr(n1c,"1","c")
    res=[]
    if(a!=""):res.append(a)
    if(b!=""):res.append(b)
    if(c!=""):res.append(c)
    if(d!=""):res.append(d)
    if(e!=""):res.append(e)
    if(f!=""):res.append(f)
    if(g!=""):res.append(g)

    troco="maq: Pode retirar o troco: "
    for i in range(0,len(res)):
        if(i==(len(res)-2)):
            troco+=res[i] + " e "
        elif(i==(len(res)-1)):
            troco+=res[i]
        else:
            troco+= res[i] + ", "
    print(troco)
    print("maq: Até à próxima")
    lexer.acabou=True
    return t



def t_SELECIONAR(t):
    r"SELECIONAR\sA\d+"
    codigo=re.search("A\d+", t.value).group()

    produto=encontraProduto(codigo)
    if(produto!=None):

        preco=produto["preco"]
        euros=int(preco)
        centimos= int((preco-euros)*100)
        #Caso tenha saldo
        if(euros<lexer.euros or (euros == lexer.euros and centimos<=lexer.centimos)):
            nomeProduto=produto["nome"]
            print(f"maq: Pode retirar o produto dispensado \"{nomeProduto}\"")
            lexer.euros-=euros
            lexer.centimos-=centimos
            if(lexer.centimos <0):
                lexer.euros-=1
                lexer.centimos+=100
            printaSaldo()
            eliminaProduto(codigo)
        else:
            print("maq: Saldo insufuciente para satisfazer o seu pedido")

            if(lexer.euros==0):
                if(euros ==0):
                    print("maq: Saldo = " + str(lexer.centimos)+"c; Pedido = " + str(centimos)+"c")
                else:
                    print("maq: Saldo = " + str(lexer.centimos)+"c; Pedido = " +str(euros)+"e"+str(centimos)+"c")
            else:
                if(euros ==0):
                    print("maq: Saldo = "+str(lexer.euros)+"e" + str(lexer.centimos)+"c; Pedido = " + str(centimos)+"c")
                else:
                    print("maq: Saldo = " +str(lexer.euros)+"e"+ str(lexer.centimos)+"c; Pedido = " +str(euros)+"e"+str(centimos)+"c")


    else:
        print("maq: Produto nao existe")
    return t

def t_MOEDA(t):
    r"MOEDA (\s*\d+e,?\s*|\s*\d+c,?\s*)+.*"
    for euros in re.findall("\d+e",t.value):
        lexer.euros+= int(euros[:-1])
    for centimos in (re.findall("\d+c",t.value)):
        lexer.centimos+= int(centimos[:-1])
        if(lexer.centimos >= 100):
            lexer.euros+=1
            lexer.centimos-=100

    printaSaldo()

    return t              



# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
lexer.euros=0
lexer.centimos=0
lexer.acabou=False






f=open("stock.json")
stock=json.load(f)


print("cod  |   nome    |   quantidade  |   preco")
print("------------------------------------------")
for produto in stock["stock"]:
    print(str(produto["cod"]) +"     " + str(produto["nome"]) +"        " + str(produto["quant"])  +"            " +  str(produto["preco"]))
print(" ")

for linha in sys.stdin:
    lexer.input(linha)
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        #print(tok)
    if(lexer.acabou==True):
        break