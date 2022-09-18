"""
Este módulo será para a minha classe Calculadora e as funções que está
Calculadora terá.

a princípio será uma calculadora básica em sua etapa inicial:
soma, subtração, multiplicação e divisão


"""


class Calculadora:

    @staticmethod
    def soma(a, b):
        return a + b

    @staticmethod
    def subtracao(a, b):
        return a - b

    @staticmethod
    def multiplicacao(a, b):
        return a * b

    @staticmethod
    def divisao(a, b):
        if a > b:
            return a / b
        return b / a
