# -----------------------------------------------------------------------------
# Name:        calculator
# Purpose:     CS 152 Python Demo
#
# This program writen upon the provided code by Author:  Rula Khayrallah
# Name: Nghi Nguyen
# SJSU ID: 010872316
# Copyright © Rula Khayrallah, 2017
# -----------------------------------------------------------------------------
"""
Simple Prefix Calculator

Evaluate simple expressions using the prefix notation.
Current version only supports addition of integers and floats.
"""


def add(operands):
    """
    Compute the sum of the operands specified if they are all numbers.
    If any operand is not a valid number, the function returns None.
    :param operands: list of strings
    :return: (int or float) the sum of the operands specified if all of them
        are valid numbers or None if an invalid number is encountered.

    """
    result = 0
    for each_operand in operands:
        each_value = get_value(each_operand)  # Get the corresponding number.
        if each_value is not None:  # Each_operand is a valid number, add it.
            result += each_value
        else:  # There is an error, return None.
            return
    return result  # Return the sum.


def sub(operands):
    """
    compute subtraction of operands
    if there is only 1 operand, return that number
    :param operands: list of strings
    :return: int or float value
    """
    result = 0
    for index, each_operand in enumerate(operands):  # loop the list of operands with index using enumerate()
        each_value = get_value(each_operand)  # get corresponding number
        if each_value is not None:
            if index == 0:
                result = each_value  # at index = 0 , set result with each value
            else:
                result -= each_value  # otherwise, result = result - each_value
        else:
            result = 0  # if operands is empty
    return result


def multiply(operands):
    """
    compute multiplication of operands
    if there is only 1 operand, return that number
    :param operands: list of strings
    :return: int or float value
    """
    result = 0
    for index, each_operand in enumerate(operands):  # loop the list of operands with index using enumerate()
        each_value = get_value(each_operand)  # get corresponding number
        if each_value is not None:
            if index == 0:
                result = each_value  # at index = 0 , set result with each value
            else:
                result *= each_value  # otherwise, result = result * each_value
        else:
            result = 0  # if operands is empty
    return result


def divide(operands):
    """
    compute division of operands
    throw error if numerator(s) is/ are
    if there is only 1 operand, return that number
    :param operands: list of strings
    :return: int or float value
    """
    result = 0
    for index, each_operand in enumerate(operands):  # loop the list of operands with index using enumerate()
        each_value = get_value(each_operand)  # get corresponding number
        if each_value is not None:
            if index == 0:  # at index = 0 , set result with each value
                result = each_value
            else:
                if each_value == 0:  # if denominator is 0, show error
                    error("non zero operand", each_value)
                    return  # break
                else:
                    result /= each_value  # otherwise, result = result / each_value
        else:
            result = 0  # if operands is empty
    return result


def comment(operands):
    """
    ignore comments with # operator
    :param operands: list of strings
    :return: none
    """
    return None


# Dictionary mapping supported symbols to functions.
# The functions must be defined above.
SUPPORTED_OPERATORS = {'+': add, '-': sub, '*': multiply, '/': divide,
                       '#': comment}  # dictionary order not consistent across machines
SUPPORTED_SYMBOLS = sorted(SUPPORTED_OPERATORS.keys())


def evaluate(expression):
    """
    Evaluate a single expression and print the result.
    :param expression: (string) simple expression in prefix notation
    :return: None
    """
    if not expression:
        return
    result = None
    # Split the expression into a list of words (tokens).
    tokens = expression.split()
    operator = tokens[0]  # in prefix notation, the operator comes first
    operands = tokens[1:]
    if operator in SUPPORTED_OPERATORS:  # SUPPORTED_OPERATORS constant (capitalized): python treat constant as variable
        function_name = SUPPORTED_OPERATORS[operator]
        result = function_name(operands)
    else:
        expected_operators = ' or '.join(SUPPORTED_SYMBOLS)
        error(expected_operators, operator)
    if result is not None:
        print(result)


def get_value(a_string):
    """
    Convert a string to a number (integer or float).
    If the given string is not a valid number, the function returns None.

    :param a_string(str)
    :return: (int or float) the corresponding number
    """
    try:
        # First try to convert the string to an integer.
        value = int(a_string)
    except ValueError:  # Not a valid integer
        try:
            # Try to convert the string to a float
            value = float(a_string)
        except ValueError:
            error('number', a_string)
            return
    return value


def error(expected, error):
    """
    Print an error message when an unexpexted token is encountered.
    :param expected: (string) supported symbols or 'number' or anything else...
    :param error: (string) the actual token encountered
    :return: None
    """
    print("Error:  expected {}, got {}".format(expected, error))
    print('Please enter a valid expression in prefix notation or q to quit')


def main():
    more_input = True
    while more_input:
        expression = input("CS 152 >>>")  # input always return a STRING, use conversion if want to use a diff type
        if expression == 'q':
            more_input = False
            print('Exiting the CS 152 Calculator')
        else:
            evaluate(expression)


if __name__ == '__main__':
    main()
