import ply.lex as lex
import sys
import re

# ? a
# b = a * 2 / (27 - 3)
# ! a + b
# c = a * b



tokens = (
    "INTERROGACAO",
    "EXCLAMACAO",
    "IGUAL",
    "MULTIPLICACAO",
    "DIVISAO",
    "SOMA",
    "SUBTRACAO",
    "LP",
    "RP",
    "NUMBER",
    "ID"
)

t_INTERROGACAO= r'\?'
t_EXCLAMACAO= r'!'
t_IGUAL= r'='
t_MULTIPLICACAO= r"\*"
t_DIVISAO= r"/"
t_SOMA= r"\+"
t_SUBTRACAO= r"-"
t_LP=r"\("
t_RP=r"\)"

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_ID(t):
    r'[a-zA-Z]\w*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_eof(t):
    r'\$'
    t.value = None  # Define o valor do token como None quando EOF é encontrado
    return t

lexer = lex.lex()

