import ply.lex as lex
tokens = [
    'ID', 'LBRACE', 'RBRACE', 'LPAREN','RPAREN',
    ]
reserved = {
    'class':'CLASS'
}
tokens+=reserved.values()

t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN =r'\('
t_RPAREN = r'\)'
t_ignore = ' \t'

def t_ID(t):
     r'[a-zA-Z_][a-zA-z0-9_]*'
     if t.value in reserved:
         t.type = reserved[t.value]
     return t



