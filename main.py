from complex_number import ComplexNumber
from operations.addition import Addition
from operations.multiplication import Multiplication
from operations.division import Division
from logger import logger


def main():
    a = ComplexNumber(3, 2)  # Ввод первого комплексного числа
    b = ComplexNumber(1, 7)  # Ввод второго комплексного числа

    addition = Addition()
    multiplication = Multiplication()
    division = Division()

    result_addition = addition.execute(a, b)
    result_multiplication = multiplication.execute(a, b)
    result_division = division.execute(a, b)

    logger.info(f"Addition result: {result_addition}")
    logger.info(f"Multiplication result: {result_multiplication}")
    logger.info(f"Division result: {result_division}")


if __name__ == "__main__":
    main()
