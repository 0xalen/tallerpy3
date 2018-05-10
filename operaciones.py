#!/usr/bin/python3
# -*- coding:utf-8 -*-
#
# Copyright 2018 Alejandro Trinidad <franco.unpa@protonmail.com>
#
# TallerPy3 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# These scripts are distributed in the hope that they will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with TallerPy3 . If not, see <http://www.gnu.org/licenses/>.
#

"""
    Módulo para la presentación de operaciones básicas que permiten usar Python
    como una calculadora.
"""

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
