import ply.yacc as yacc
import ply.lex as lex
import langlex
from langlex import tokens

def p_program(p):
    '''program : CLASS ID LBRACE classdef RBRACE'''

def p_classdef(p):
    '''classdef : ID'''
    print(p[
