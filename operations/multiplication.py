from .operation import Operation
from complex_number import ComplexNumber


class Multiplication(Operation):
    def execute(self, a, b):
        real = a.real * b.real - a.imaginary * b.imaginary
        imaginary = a.real * b.imaginary + a.imaginary * b.real
        return ComplexNumber(real, imaginary)
