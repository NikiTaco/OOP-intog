from .operation import Operation
from complex_number import ComplexNumber


class Addition(Operation):
    def execute(self, a, b):
        real = a.real + b.real
        imaginary = a.imaginary + b.imaginary
        return ComplexNumber(real, imaginary)
