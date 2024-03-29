import ply.lex as lex

tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'OPERATORS',
    'ATRIBUTE',
    'DELIMITER',
    'NUMBER'
)

t_SELECT = r'(?i)select'
t_FROM = r'(?i)from'
t_WHERE = r'(?i)where'
t_OPERATORS = r'[=<>]+'
t_ATRIBUTE = r'\w+'
t_DELIMITER = r','

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

data = "Select id, nome, salario From empregados Where salario >= 820"

lexer = lex.lex()

lexer.input(data)

for tok in lexer:
    print(tok.type, tok.value, tok.lineno, tok.lexpos)