# -----------------------------------------------------------------------------
# Name:        pluto2
# extended from pluto1.py - author: Rula Khayrallah
#
# Author: Jennifer  Nghi Nguyen - SJSU ID: 010872316
#
# -----------------------------------------------------------------------------
"""
Recursive descent parser to recognize & evaluate simple arithmetic expressions

Supports the following grammar:
    <command> ::= <bool_expr>
    <bool_expr> ::= <bool_term> {OR <bool_term>}
    <bool_term> ::= <not_factor> {AND <not_factor>}
    <not_factor> ::= {NOT} <bool_factor>
    <bool_factor> ::= BOOL | LPAREN <bool_expr> RPAREN | <comparison>
    <comparison> ::= <arith_expr> [COMP_OP <arith_expr>]
    <arith_expr> ::= <term> {ADD_OP <term>}
    <term> ::= <factor> {MULT_OP <factor>}
    <factor> ::= LPAREN <arith_expr> RPAREN | FLOAT | INT
"""
from operator import add, sub, mul, truediv
from operator import lt, gt, eq, ne, le, ge
from operator import not_, or_, and_

import lex

# List of token names - required
tokens = ('FLOAT', 'INT',
          'ADD_OP', 'MULT_OP',
          'LPAREN', 'RPAREN',
          'OR', 'AND',
          'NOT', 'BOOL',
          'COMP_OP')

# global variables
token = None
lexer = None
parse_error = False

# Regular expression rules for simple tokens
# r indicates a raw string in Python - less backslashes
t_COMP_OP = r'<=|>=|!=|==|<|>'
t_ADD_OP = r'\+|-'
t_MULT_OP = r'\*|/'
t_NOT = r'not'
t_AND = r'and'
t_OR = r'or'
t_LPAREN = r'\('
t_RPAREN = r'\)'


# Regular expression rules with some action code
# The order matters
def t_FLOAT(t):
    r'\d*\.\d+|\d+\.\d*'
    t.value = float(t.value)  # string must be converted to float
    return t


def t_INT(t):
    r'\d+'
    t.value = int(t.value)  # string must be converted to int
    return t


# function for boolean tokens
def t_BOOL(t):
    r'True|False'

    if t.value == "True":
        t.value = True # value of t is boolean type
    elif t.value == "False":
        t.value = False
    return t


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Lexical error handling rule
def t_error(t):
    global parse_error
    parse_error = True
    print("ILLEGAL CHARACTER: {}".format(t.value[0]))
    t.lexer.skip(1)


# For homework 2, add the comparison operators to this dictionary
SUPPORTED_OPERATORS = {'+': add, '-': sub, '*': mul, '/': truediv,
                       '<': lt, '>': gt, '==': eq, '<=': le, '>=': ge, '!=': ne,  # COMP_OP
                       'or': or_, 'and': and_, 'not': not_}  # boolean op


def command():
    """
     <command> ::= <bool_expr>

    """
    result = bool_expr()
    if not parse_error:
        if token:
            error("END OF COMMAND OR OPERATOR")
        else:
            print(result)


def bool_expr():
    """
     <bool_expr> ::= <bool_term> {OR <bool_term>}
    """
    result = bool_term()
    while token and token.type == 'OR':
        operation = SUPPORTED_OPERATORS[token.value]
        match()  # get next token
        operand = bool_term()
        if not parse_error:
            result = operation(result, operand)  # or_(a,b)
    return result


def bool_term():
    """
    <bool_term> ::= <not_factor> {AND <not_factor>}
    """
    result = not_factor()
    while token and token.type == 'AND':
        operation = SUPPORTED_OPERATORS[token.value]
        match()  # next token
        operand = bool_term()
        if not parse_error:
            result = operation(result, operand)  # and_(a,b)
    return result


def not_factor():
    """
    <not_factor> ::= {NOT} <bool_factor>
    """
    result = ""
    count = 0  # counter keep track of repetition of not

    # if token doesn't start with not
    if token and token.type != 'NOT':
        result = bool_factor()  # process <bool_factor>

    # if token start with not
    if token and token.type == 'NOT':
        operation = SUPPORTED_OPERATORS[token.value]  # not_()
        while token and token.type == 'NOT':
            count += 1  # increment the count
            match()  # next token
        operand = bool_factor()  # <bool_factor>
        if not parse_error:

            # use not_(operand)
            for i in range(0, count):
                result = operation(operand)
                operand = result

    return result


def bool_factor():
    """
    <bool_factor> ::= BOOL | LPAREN <bool_expr> RPAREN | <comparison>
    """

    # BOOL
    if token and token.type == 'BOOL':
        result = token.value
        match() # next token
        return result

    # LPAREN <bool_expr> RPAREN
    elif token and token.type == 'LPAREN':
        match() # next token
        result = bool_expr()
        if token and token.type == 'RPAREN':
            match()  # next token
            return result
        else:
            error(')')

    # <comparison>
    else:
        result = comparison()

    return result


def comparison():
    """
     <comparison> ::= <arith_expr> [COMP_OP <arith_expr>]
    """
    result = arith_expr()
    if token and token.type == 'COMP_OP':
        operation = SUPPORTED_OPERATORS[token.value]  # comparision functions
        match()  # next token
        operand = arith_expr()
        if not parse_error:
            result = operation(result, operand)
    return result


def arith_expr():
    """
    <arith_expr> ::= <term> {ADD_OP <term>}
    """
    result = term()
    while token and token.type == 'ADD_OP':
        operation = SUPPORTED_OPERATORS[token.value]  # add/minus functions
        match()  # next token
        operand = term()
        if not parse_error:
            result = operation(result, operand)
    return result


def term():
    """
    <term> ::= <factor> {MULT_OP <factor>}
    """
    result = factor()
    while token and token.type == 'MULT_OP':
        operation = SUPPORTED_OPERATORS[token.value]  # *,/ functions
        match()  # next token
        operand = factor()
        if not parse_error:
            result = operation(result, operand)
    return result


def factor():
    """
     <factor> ::= LPAREN <arith_expr> RPAREN | FLOAT | INT
    """
    # LPAREN <arith_expr> RPAREN
    if token and token.type == 'LPAREN':
        match()
        result = arith_expr()
        if token and token.type == 'RPAREN':
            match()
            return result
        else:
            error(')')

    # FLOAT or INT
    elif token and (token.type == 'FLOAT' or token.type == 'INT'):
        result = token.value
        match()
        return result
    else:
        error('NUMBER')


def match():
    """
    Get the next token
    """
    global token
    token = lexer.token()


def error(expected):
    """
    Print an error message when an unexpected token is encountered, sets
    a global parse_error variable.
    :param expected: (string) '(' or 'NUMBER' or or ')' or anything else...
    :return: None
    """
    global parse_error
    if not parse_error:
        parse_error = True
        print('Parser error')
        print("Expected:", expected)
        if token:
            print('Got: ', token.value)
            print('line', token.lineno, 'position', token.lexpos)


def main():
    global token
    global lexer
    global parse_error
    # Build the lexer
    lexer = lex.lex()
    # Prompt for a command
    more_input = True
    while more_input:
        input_command = input("Pluto 2.0>>>")
        if input_command == 'q':
            more_input = False
            print('Bye for now')
        elif input_command:
            parse_error = False
            # Send the command to the lexer
            lexer.input(input_command)
            token = lexer.token()  # Get the first token in a global variable
            command()


if __name__ == '__main__':
    main()
