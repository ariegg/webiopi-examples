#   Copyright 2016 Andreas Riegg - t-h-i-n-x.net
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#   WebIOPi test script for all kinds of macros
#
#   NOTE: Macros that are called via REST "POST .../macros/macroname..." 
#   are called by WebIOPi by using macro(*args) or macro() if REST path 
#   has no agrument values at the end.
#   Thus, using keyword arguments via macro(**kwargs) is not possible
#   at the moment.

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

