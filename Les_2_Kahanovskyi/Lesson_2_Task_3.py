class Point():

    def __init__(self, x, y, z):

        self._x = x
        self._y = y
        self._z = z


    def __add__(self, other_x, other_y, other_z):

       return  (other_x + self._x, other_y + self._y, other_z + self._z)


    def __sub__(self, other_x, other_y, other_z):

       return  (self._x - other_x, self._y - other_y, self._z - other_z)


    def __mul__(self, other_x, other_y, other_z):

        return (other_x * self._x, other_y * self._y, other_z * self._z)


    def __truediv__(self, other_x, other_y, other_z):

        return (self._x / other_x, self._y / other_y, self._z / other_z)


    def __str__(self):

        return f' (x = {self._x}, y = {self._y}, z = {self._z}) '


point = Point(1, 2, 3)
print(point)

print(f' add = {point.__add__(1, 2, 3)}')
print(f' sub = {point.__sub__(1, 2, 3)}')
print(f' mul = {point.__mul__(1, 2, 3)}')
print(f' div = {point.__truediv__(1, 2, 3)}')