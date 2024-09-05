import operator
def calculate():
    operation = input('''
Por favor digite a operação matematica que você deseja realizar:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

    number_1 = float(input('Entre o seu 1º número: '))
    number_2 = float(input('Entre o seu 2º número: '))

    if operation == '+':
        result = number_1 + number_2
        print('{} + {} = {}'.format(number_1, number_2,result))
        

    elif operation == '-':
        result = number_1 - number_2
        print('{} - {} = {}'.format(number_1, number_2,result))

    elif operation == '*':
        result = number_1 * number_2
        print('{} * {} = {}'.format(number_1, number_2,result))

    elif operation == '/':
        result = number_1 / number_2
        print('{} / {} = {}'.format(number_1, number_2,result))

    else:
        print('Você não digitou um operador válido, por favor rode o programa novamente.')

    again()

def again():
    calc_again = input('''
Você deseja realizar um novo cálculo?
Por favor digite S para SIM e N para NÃO.
''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('Até mais.')
    else:
        again()

calculate()