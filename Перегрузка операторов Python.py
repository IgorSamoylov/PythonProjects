

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self, other):
        if not isinstance(other, Vector):
            return "Not a Vector!"
        
        return self.x < other.x and self.y < other.y

vector1 = Vector(10, 23)
vector2 = Vector(15, 43)
print(vector1 < vector2)


print(vector1 < "Йоу")
