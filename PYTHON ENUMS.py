
# Basic approach

class Color:
    RED = 1
    BLACK = 2
    WHITE = 3
    YELLOW = 4


if Color.RED == Color.RED:
    print("OK")


# Using enum library

import enum

class ColorE(enum.Enum):
    RED = 1
    BLACK = 2
    WHITE = 3
    YELLOW = 4

# Using 'is' comparison
if ColorE.YELLOW is ColorE.YELLOW:
    print("OK")
    
# Iterating over values
for color in ColorE:
    print(color)


# Add custom attributes
class ColorEA(enum.Enum):
    RED = (1, "Red color")
    BLACK = (2, "Black color")
    WHITE = (3, "White color")
    YELLOW = (4, "Yellow color")

    def __init__(self, id, phrase):
        self.id = id
        self.phrase = phrase

print(ColorEA.WHITE.phrase)
