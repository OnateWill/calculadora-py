from funcoes import Calculadora
res = 0
recurso = True

while recurso != 'sair':
    recurso = input('Qual recurso deseja usar?'
                    'soma, subtração, multiplicação, divisão: ').strip().lower()
    num1 = float(input('Digite um valor numérico: '))
    if recurso == 'soma':
        res = Calculadora.soma(res, num1)
    elif recurso == 'subtração':
        res = Calculadora.subtracao(res, num1)
    elif recurso == 'multiplicação':
        res = Calculadora.multiplicacao(res, num1)
    elif recurso == 'divisão':
        res = Calculadora.divisao(res, num1)

    print(res)
