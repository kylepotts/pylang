import ply.lex as lex
tokens = [
    'ID', 'LBRACE', 'RBRACE', 'LPAREN','RPAREN','SEMICOLON','COMMA',
    ]
reserved = {
    'class':'CLASS',
    'int': 'INT',
    'def': 'DEF',
}
tokens+=reserved.values()

t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN =r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_COMMA = r','
t_ignore = ' \t'

def t_ID(t):
     r'[a-zA-Z_][a-zA-z0-9_]*'
     if t.value in reserved:
         t.type = reserved[t.value]
     return t

def t_newline(t):
     r'\n+'
     t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal Character '%s'" % t.value[0])
    t.lexer.skip(1)
