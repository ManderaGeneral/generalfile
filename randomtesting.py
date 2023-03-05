
from generalfile import *



x = None

try:
    Path("hello:there")
except InvalidCharacterError as e:
    x = e

assert isinstance(x, InvalidCharacterError)
