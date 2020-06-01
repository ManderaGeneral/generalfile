"""
Random local testing
"""

from generalfile.base.classfile import File
from test.base.setUpWorkDir import SetUpWorkDir
from generallibrary.types import typeChecker
import pandas as pd

# SetUpWorkDir.activate()
# File.openFolder("")

# print(File.getWorkingDir())

# print(pd.DataFrame().__class__)
# print(pd.DataFrame)



import re
from math import sqrt

ignore = ["+", "-", "*", "/", "(", ")", "sqrt"]

def tokenize(expression):
    return re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\-\/])", expression)

def calculate(expression, *args):
    seenArgs = {}
    newTokens = []
    tokens = tokenize(expression)
    for token in tokens:
        try:
            float(token)
        except ValueError:
            tokenIsFloat = False
        else:
            tokenIsFloat = True

        if token in ignore or tokenIsFloat:
            newTokens.append(token)
        else:
            if token not in seenArgs:
                seenArgs[token] = str(args[len(seenArgs)])
            newTokens.append(seenArgs[token])
    return eval("".join(newTokens))

print(calculate("-1* beta * s * i", 1, 2, 3))
print(calculate("5.5 * x * x", 3))
print(calculate("sqrt(x) * y", 9, 2))

