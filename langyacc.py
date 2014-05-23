#! /usr/bin/python2.7
import ply.yacc as yacc
import ply.lex as lex
import langlex
from langlex import tokens

def p_program(p):
    '''program : CLASS ID LBRACE classdef RBRACE'''

def p_classdef(p):
    '''classdef : functionOrVarList'''

def p_functionOrVarList(p):
    '''functionOrVarList : functionOrVarList function
                         | functionOrVarList globalVar
                         |
                        '''

def p_globalVar(p):
    '''globalVar : ID varType SEMICOLON'''
    print("GlobalVar= "+p[1])
    print("Type= "+p[2])

def p_function(p):
    '''function : functionWithReturnType
                | functionWithoutReturnType'''

def p_functionWithReturnType(p):
    ''' functionWithReturnType : DEF ID LPAREN arguments  RPAREN varType LBRACE RBRACE'''

def p_functionWithoutReturnType(p):
    '''functionWithoutReturnType : DEF ID LPAREN arguments RPAREN LBRACE RBRACE'''
    print('function ' + p[2])


def p_arguments(p):
    '''arguments : argList
                 |
                 '''


def p_argList(p):
    '''argList : arg
               | argList COMMA arg'''

def p_arg(p):
    ''' arg : ID varType'''

def p_VarType(p):
    '''varType : INT'''
    p[0] = p[1]


lex.lex(module=langlex)
yacc.yacc()

yacc.parse('class Now { a int; def call(){} }')
