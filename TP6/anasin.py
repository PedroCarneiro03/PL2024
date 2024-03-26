from analex import lexer
import ply.lex as lex



prox_simb=("Erro", "",0,0)

def parserError(s):
    print("Erro sintatico:",s)

def rec_term(simb):
    global prox_simb
    if prox_simb.type == simb:
        prox_simb=lexer.token()
    else:
        parserError(simb)

def rec_Linguagem():
    global prox_simb
    if prox_simb.type == "INTERROGACAO":
        rec_term("INTERROGACAO")
        rec_term("ID")
        print("Reconheci P1: Linguagem -> ? id")
    elif prox_simb.type == "EXCLAMACAO":
        rec_term("EXCLAMACAO")
        rec_Conteudo()
        print("Reconheci P2: Linguagem -> ! Conteudo")
    elif prox_simb.type == "ID":
        rec_term("ID")
        rec_term("IGUAL")
        rec_Conteudo()
        print("Reconheci P3: Linguagem -> id = Conteudo")
    else:
        parserError(prox_simb)


def rec_Conteudo():
    global prox_simb
    if prox_simb.type == "ID":
        rec_term("ID")
        rec_Resto()
        print("Reconheci P4: Conteudo -> id Resto")
    elif prox_simb.type == "NUMBER":
        rec_term("NUMBER")
        rec_Resto()
        print("Reconheci P5: Conteudo -> num Resto")
    elif prox_simb.type == "LP":
        rec_term("LP")
        rec_Conteudo()
        rec_term("RP")
        print("Reconheci P6: Conteudo -> ( Conteudo )")
    else:
        parserError(prox_simb)


def rec_Resto():
    global prox_simb
    if prox_simb.type == "SOMA":
        rec_term("SOMA")
        rec_Conteudo()
        print("Reconheci P7: Resto -> + Conteudo")
    elif prox_simb.type == "SUBTRACAO":
        rec_term("SUBTRACAO")
        rec_Conteudo()
        print("Reconheci P8: Resto -> - Conteudo")
    elif prox_simb.type == "MULTIPLICACAO":
        rec_term("MULTIPLICACAO")
        rec_Conteudo()
        print("Reconheci P9: Resto -> * Conteudo")
    elif prox_simb.type == "DIVISAO":
        rec_term("DIVISAO")
        rec_Conteudo()
        print("Reconheci P10: Resto -> / Conteudo")
    elif prox_simb.type=="eof" or prox_simb.type == "RP":
        print("Reconheci P11: Resto -> &")
    else:
        parserError(prox_simb)


def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb=lexer.token()
    rec_Linguagem()
    print("Ta tudo fixe")





# Programa de Teste
linha1="? a"
linha2="b = a * 2 / (27 - 3)"
linha3="! a + b"
linha4="c = a * b"
rec_Parser(linha1)
rec_Parser(linha2)
rec_Parser(linha3)
rec_Parser(linha4)