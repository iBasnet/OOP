# Object Oriented Programming in Python

class complex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, number):
        real = self.real + number.real
        imag = self.imag + number.imag
        result = complex(real, imag)
        return result


n1 = complex(2, 4)
n2 = complex(1, 1)
result = n1.add(n2)
print("real =", result.real)
print("imag =", result.imag)
