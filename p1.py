# p1.py
# Autora: Joelma Godoy
# Compilador LALG em Python
# Técnica: Análise Sintática Ascendente (LALR(1)) com PLY (Yacc)

import ply.lex as lex
import ply.yacc as yacc

# ==================================================
# ANÁLISE LÉXICA
# ==================================================

tokens = (
    'ID', 'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQUAL',
    'LPAREN', 'RPAREN',
    'PRINT', 'INPUT',
)

t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = ' \t'

def t_PRINT(t): r'print'; return t
def t_INPUT(t): r'input'; return t
def t_ID(t): r'[a-zA-Z_]\w*'; return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Erro léxico: caractere inválido '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# ==================================================
# GERAÇÃO DE CÓDIGO PARA MÁQUINA HIPOTÉTICA
# ==================================================

codigo_objeto = []
tabela_simbolos = {}

def emit(instrucao):
    codigo_objeto.append(instrucao)

def declarar_variavel(var):
    if var not in tabela_simbolos:
        tabela_simbolos[var] = len(tabela_simbolos)
        emit("ALME 1")

# ==================================================
# ANÁLISE SINTÁTICA ASCENDENTE (LALR)
# ==================================================

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

def p_programa(p):
    'programa : comandos'
    emit("PARA")

def p_comandos(p):
    '''comandos : comando comandos
                | comando'''
    pass

def p_comando_atribuicao(p):
    'comando : ID EQUAL expressao'
    declarar_variavel(p[1])
    emit(f"ARMZ {tabela_simbolos[p[1]]}")

def p_comando_print(p):
    'comando : PRINT LPAREN expressao RPAREN'
    emit("IMPR")

def p_expressao_binaria(p):
    '''expressao : expressao PLUS expressao
                 | expressao MINUS expressao
                 | expressao TIMES expressao
                 | expressao DIVIDE expressao'''
    if p[2] == '+': emit("SOMA")
    elif p[2] == '-': emit("SUBT")
    elif p[2] == '*': emit("MULT")
    elif p[2] == '/': emit("DIVI")

def p_expressao_num(p):
    'expressao : NUMBER'
    emit(f"CRCT {p[1]}")

def p_expressao_id(p):
    'expressao : ID'
    declarar_variavel(p[1])
    emit(f"CRVL {tabela_simbolos[p[1]]}")

def p_expressao_input(p):
    'expressao : INPUT LPAREN RPAREN'
    emit("LEIT")

def p_error(p):
    print("Erro sintático.", p)

parser = yacc.yacc()

# ==================================================
# EXECUÇÃO
# ==================================================

if __name__ == "__main__":
    with open("codigoPraCompilar.txt", "r", encoding="utf-8") as f:
        fonte = f.read()

    emit("INPP")
    parser.parse(fonte)

    with open("codigoCompilado.txt", "w", encoding="utf-8") as arq:
        arq.write("\n".join(codigo_objeto))

    print("✔ Código objeto gerado com sucesso.")
