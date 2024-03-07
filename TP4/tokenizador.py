import sys
import re
import ply.lex as lex

tokens = (
   'NUMBER',
   'FUNCAO',
   'OPERACAO',
   'ID'
)


# Regular expression rules for simple tokens
t_FUNCAO = r'(?i)select|where|from'
t_OPERACAO =r"[><]?="
t_ID   = r'\w+'


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
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

dados="Select id, nome, salario from empregados where salario >= 820"

lexer.input(dados)

while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
