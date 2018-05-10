# operaciones.python
#!/usr/bin/python3
from random import randint

def obtenerNumero():
      return randint(1,99)

def suma(num1, num2):
    print('''Suma (+):
    ''',num1,''' + ''',num2,''' = ''',num1+num2)

def resta(num1, num2):
    print('''Resta (-):
    ''',num1,''' - ''',num2,''' = ''',num1-num2)

def producto(num1, num2):
    print('''Producto (*):
    ''',num1,''' * ''',num2,''' = ''',num1*num2)

def division(num1, num2):
    print('''División (/):
    ''',num1,''' / ''',num2,''' = ''',num1/num2)

def divisionPiso(num1, num2):
    print('''División piso (//):
    ''',num1,''' // ''',num2,''' = ''',num1//num2)

def modulo(num1, num2):
    print('''Modulo (%):
    ''',num1,''' % ''',num2,''' = ''',num1%num2)

def divisionTeorema(num1, num2):
    print('''DIVIDENDO = DIVISOR * COCIENTE + RESTO
            num1 = num2 * (num1 // num2) + num1 % num2
            ''',num1,''' = ''',num2,''' * ''',num1//num2,''' +''',num1%num2)

def potencia(num1, num2):
    print('''Potencia (**):
    ''',num1,''' ** ''',num2,''' = ''',num1**num2)

def ordenDeOperaciones(num1, num2):
    print('''PEMDAS:
    * Paréntes
    * Exponentes
    * Multiplicación
    * División
    * Adición
    * Substracción

    Ejemplo:
    ''',num1,''' + ''',num2,''' / ''',num2,''' = ''',num1+num2/num2,'''
    (''',num1,''' + ''',num2,''') / ''',num2,''' = ''',(num1+num2)/num2)
