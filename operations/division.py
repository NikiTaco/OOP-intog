from .operation import Operation
from complex_number import ComplexNumber


class Division(Operation):
    def execute(self, a, b):
        denom = b.real**2 + b.imaginary**2
        real = (a.real * b.real + a.imaginary * b.imaginary) / denom
        imaginary = (a.imaginary * b.real - a.real * b.imaginary) / denom
        return ComplexNumber(real, imaginary)
