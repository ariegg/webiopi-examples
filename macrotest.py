# Test script for all kinds of macros
# NB: Macros are called via REST by using macro(*args) or macro() if path has no values

import webiopi

@webiopi.macro
def macroWithoutArguments():
    print("n/a")
    return "OK"

@webiopi.macro
def macroWithTwoArguments(a, b):
    print(a)
    print(b)
    return "OK"

@webiopi.macro
def macroWithTwoSecondHasDefaultArguments(a, b=2):
    print(a)
    print(b)
    return "OK"

@webiopi.macro
def macroWithTwoBothHaveDefaultArguments(a=1, b=2):
    print(a)
    print(b)
    return "OK"

@webiopi.macro
def macroWithStarOnlyArguments(*a):
    print(a)
    for arg in a:
        print(arg)
    return "OK"

@webiopi.macro
def macroWithOnePositionalAndStarArguments(a, *b):
    print(a)
    print(b)
    return "OK"

@webiopi.macro
def macroWithOnePositionalWithDefaultAndStarArguments(a=1, *b):
    print(a)
    print(b)
    return "OK"

@webiopi.macro
def macroWithTwoPositionalSecondHasDefaultAndStarArguments(a, b=2, *c):
    print(a)
    print(b)
    print(c)
    return "OK"

