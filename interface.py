from funcoes import Calculadora

print('Seja Bem-vindo a v.1 da minha calculadora \n'
      'nota: O primeiro valor de qualquer recurso será 0.\n')

res = 0
print(f"Display: {res}\n")
recurso = ''


while recurso != 'sair':
    recurso = input('Qual recurso deseja usar?\n'
                    'soma, subtração, multiplicação, divisão: ').strip().lower()

    if recurso in ['soma', 'subtração', 'multiplicação', 'divisão']:
        num1 = float(input('Digite um valor numérico: '))
        if recurso == 'soma':
            res = Calculadora.soma(res, num1)
        elif recurso == 'subtração':
            res = Calculadora.subtracao(res, num1)
        elif recurso == 'multiplicação':
            res = Calculadora.multiplicacao(res, num1)
        elif recurso == 'divisão':
            res = Calculadora.divisao(res, num1)
        print(f'-----------------------------------------------')
        print(f"\nDisplay: {res}\n")
        print(f'-----------------------------------------------')
