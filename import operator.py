import operator

dict_operadores = {
'+': operator.add,
'-': operator.sub,
'*': operator.mul,
'/': operator.truediv,
}

print ("digite um número")
numero1 = int(input( ))

print("digite um operador")
operador = (input( ))

print("digite um segundo número")
numero2 = int(input( ))
resultado = (dict_operadores[operador](numero1,numero2))

print("o resultado é",resultado)