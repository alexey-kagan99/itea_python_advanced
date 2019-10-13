class MyStack:
    def __init__(self):

        self.container = []

    def is_empty(self):

        if self.size() == 0:

            return True

    def push(self, item):
        self.container.append(item)

    def pop(self):

        return self.container.pop()

    def size(self):
        return len(self.container)

    def show(self):

        return self.container


class MyQue(MyStack):

    def __init__(self):

        super().__init__()

    def pop(self):

        self.container.pop(0)


class Complex():

    def __init__(self, re, im):

        self.re = re
        self.im = im

    def get_num(self):

        return self.re, self.im

    def __add__(self, other_re, other_im):

        return f' z = {other_re + self.re} + {other_im + self.im}i '

    def __sub__(self, other_re, other_im):

        return f' z = {self.re - other_re} + {self.im - other_im}i '

    def __mul__(self, other_re, other_im):

        return f' z = {(self.re * other_re - self.im * other_im)} + {(self.re * other_im + self.im * other_re)}i '

    def __truediv__(self, other_re, other_im):

        return f' z = {(self.re * other_re + self.im * other_im) / (other_re ** 2 + other_im ** 2)} + {(self.im * other_re - self.re * other_im) / (other_re ** 2 + other_im ** 2)}i '

    def __str__(self):

        return f' {self.re} + {self.im}i '


print(' Stack ')
new_stack = MyStack()
new_stack.push('1')
new_stack.push('2')

print(f' in container {new_stack.show()}')
new_stack.push('3')
print(f' in container {new_stack.show()} ')

print(f' {new_stack.pop()} is deleted ')
print(f' in container {new_stack.show()} ')

new_stack.push('4')
print(f' in container {new_stack.show()}')

print(' Que ')
new_que = MyQue()

new_que.push('1')
new_que.push('2')

print(f' in container {new_que.show()}')
new_que.push('3')
print(f' in container {new_que.show()} ')

print(f' {new_que.pop()} is deleted ')
print(f' in container {new_que.show()} ')

new_que.push('4')
print(f' in container {new_que.show()}')

print(' Complex ')
z_1 = Complex(5, 7)
z_2 = Complex(3, 1)
print(f' z1 = {z_1} ')
print(f' z2 = {z_2} ')

print(z_1.__add__(int(z_2.get_num()[0]), int(z_2.get_num()[1])))
print(z_1.__sub__(int(z_2.get_num()[0]), int(z_2.get_num()[1])))
print(z_1.__mul__(int(z_2.get_num()[0]), int(z_2.get_num()[1])))
print(z_1.__truediv__(int(z_2.get_num()[0]), int(z_2.get_num()[1])))


