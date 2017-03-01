# -----------------------------------------------------------------------------
# Name:        scanner
#
# Purpose:     CS 152 - Demonstrate the use of lex to generate a scanner
#
# -----------------------------------------------------------------------------
"""
A Simple Scanner

Scans simple arithmetic expressions with floats and integers.
Supports +, -, * and /
"""
import lex

# Regular expression rules for simple tokens
# r indicates a raw string in Python - less backslashes
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'


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


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("ILLEGAL CHARACTER: {}".format(t.value[0]))
    t.lexer.skip(1)


def main():
    # List of token names - required
    tokens = ('FLOAT', 'INT', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE')
    # Build the lexer
    lexer = lex.lex()
    # Prompt for an expression
    expression = input("CS 152 Scanner>>>")
    # Send the expression to the lexer
    lexer.input(expression)
    for token in lexer:
        print(token)


if __name__ == '__main__':
    main()
