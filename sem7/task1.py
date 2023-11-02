class Vector:
    def __init__(self, string):
        x, y, z = list(map(float, string.split(',')))
        if isinstance(x, (float, int)) and isinstance(y, (float, int)) and isinstance(z, (float, int)):
            self.x = x
            self.y = y
            self.z = z
        else:
            print("Syntax Error")
            exit(0)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x - other, self.y - other, self.z - other)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z

    def __rmul__(self, k):
        return Vector(k * self.x, k * self.y, k * self.z)

    def __radd__(self, other):
        return self + other

    def __repr__(self):
        return f'{self.x} {self.y} {self.z}'


def cmass(*args):
    X = 0
    Y = 0
    Z = 0
    if isinstance(args[0], Vector):
        for i in range(len(args)):
            X = X * i / (i + 1) + args[i].x / (i + 1)
            Y = Y * i / (i + 1) + args[i].y / (i + 1)
            Z = Z * i / (i + 1) + args[i].z / (i + 1)
        return Vector(str(str(X) + ', ' + str(Y) + ', ' + str(Z)))
    return


def triangle_square(*args):
    max_square = 0
    if isinstance(args[0], Vector):
        for i in range(0, len(args)):
            for j in range(i + 1, len(args)):
                for k in range(j + 1, len(args)):
                    vector1 = args[j] - args[i]
                    vector2 = args[k] - args[i]
                    square = ((vector1.x * vector2.y - vector1.y * vector2.x) ** 2 + (
                                vector1.x * vector2.z - vector2.x * vector1.z) ** 2 + (
                                          vector1.y * vector2.z - vector1.z * vector2.y) ** 2) ** 0.5
                    if square > max_square:
                        max_square = square
                    else:
                        continue
    if max_square == 0:
        return "Error"
    else:
        return max_square


vectors = []
s = input()
while (s != '0'):
    s.replace('{', '')
    s.replace('}', '')
    x, y, z = list(map(float, s.split(',')))
    v = Vector(str(x) + ',' + str(y) + ',' + str(z))
    vectors.append(v)
    s = input()

victors = tuple(vectors)

print(cmass(*victors))
print(triangle_square(*victors))
# Когда заканчивается ввод векторов, на новой строке нужно ввести 0
